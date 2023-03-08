/*
 * Display: https://randomnerdtutorials.com/esp8266-0-96-inch-oled-display-with-arduino-ide/
 * GPS: https://diy-project.tistory.com/55
 * SD: https://diyi0t.com/sd-card-arduino-esp8266-esp32/
 * ESP-examples: https://arduino-esp8266.readthedocs.io/en/latest/esp8266wifi/scan-examples.html
 * Library Display: https://github.com/vlast3k/Arduino-libraries/tree/master/SSD1306
 * Reference Github: https://github.com/AlexLynd/ESP8266-Wardriving
 * 
 * 
 * GPIO 0=D3(connect Tx of GPS) and GPIO 2=D4(Connect Rx of GPS)
 * RX D4
 * TX D3    ---->GPS
 * VCC 5V
 * GND GND
 * 
 * GND GND
 * VCC 3.3V ----> DISPLAY
 * SCK D1
 * SDA D2
 * 
 * GND GND
 * VCC 5V
 * MISO D6  ----> SD
 * MOSI D7
 * SCK D5
 * CS D8
*/
#include <ESP8266WiFi.h>
#include <SD.h>
#include <SPI.h>
#include <TinyGPSPlus.h>
#include <SoftwareSerial.h>
#include "SSD1306Wire.h"
#include <string.h>

String latitude = "";
String longitude = "";
const uint32_t GPSBaud = 9600;
// Oggetto per gestire le informazioni GPS
TinyGPSPlus gps;
static const int RXPin = 0, TXPin = 2;
//SoftwareSerial ss(RXPin, TXPin); // the serial interface to the GPS device 
SoftwareSerial ss(RXPin, TXPin); // the serial interface to the GPS device 

String filename = "";
int networks = 0;

//counter total wifi found
int counter = 0;

#define LOG_RATE 500
char currentTime[5];

SSD1306Wire display(0x3c, SDA, SCL);
#define SD_CS D8

void setup(){
  Serial.begin(115200);
  display.init();
  display.flipScreenVertically();
  display.setFont(ArialMT_Plain_16);
  display.setTextAlignment(TEXT_ALIGN_RIGHT);
  ss.begin(GPSBaud);
  Serial.print("Initializing SD card...");
  if (!SD.begin(SD_CS)) {
    Serial.println("Initialization SD failed!");
    display.drawString(105, 17, "SD problem");
    display.display();
    delay(500);
    display.clear();
    while (!SD.begin(SD_CS));
  }
  Serial.println("Initialization SD done.");
  display.drawString(105, 17, "SD detected");
  display.display();
  delay(500);
  Serial.println("Checking GPS...");
  checkGPS();
  display.clear();
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  initializeSD();
  display.drawString(127, 30, "Initialization done");
  display.display(); 
  delay(1500);
  display.clear();
}

void checkGPS(){
  if (millis() > 5000 && gps.charsProcessed() < 10)
  {
    Serial.println(F("No GPS detected: check wiring."));
    display.drawString(108, 33, "GPS problem");
    display.display();
    delay(500);
    display.clear();
  }else{
    Serial.println(F("GPS detected"));
    display.drawString(108, 33, "Gps detected");
    display.display();
    delay(500);
    display.clear();
  }
}

void lookForNetworks(double lat, double lng){
  display.flipScreenVertically();
  display.setFont(ArialMT_Plain_16);
  display.setTextAlignment(TEXT_ALIGN_RIGHT);
  String dataString = "";
  String ssid;
  int32_t rssi;
  uint8_t encryptionType;
  uint8_t* bssid;
  int32_t channel;
  bool hidden;

  Serial.println(F("Starting WiFi scan..."));

  int n = WiFi.scanNetworks();
  counter += n;

  if (n == 0) {
    Serial.println(F("No networks found"));
  }
  else {
    Serial.printf(PSTR("%d networks found:\n"), n);
    display.drawString(102, 13, "d0raCatch");
    display.setFont(ArialMT_Plain_10);
    display.drawString(46, 29, "Latitude: ");
    //display.drawString(120, 29, String(gps.location.lat()));
    display.drawString(56, 39, "Longitude: ");
    //display.drawString(120, 39, String(gps.location.lng()));
    display.drawString(56, 50, "Wifi found: ");
    display.drawString(120, 50, String(counter));
    File file = SD.open(filename, FILE_WRITE);
    for (int8_t i = 0; i < n; i++) {
      WiFi.getNetworkInfo(i, ssid, encryptionType, rssi, bssid, channel, hidden);
      Serial.printf(PSTR("  %02d: [CH %02d] [%02X:%02X:%02X:%02X:%02X:%02X] %ddBm %c %c %s\n"), i, channel, bssid[0], bssid[1], bssid[2], bssid[3], bssid[4], bssid[5], rssi, (encryptionType == ENC_TYPE_NONE) ? ' ' : '*', hidden ? 'H' : 'V', ssid.c_str());
      //File file = SD.open(filename, FILE_WRITE);
      file.print('['+WiFi.BSSIDstr(i)+']');  
      file.print(',');
      file.print(WiFi.SSID(i));
      file.print(',');
      file.print(getEncryption(i,""));
      file.print(',');
      file.print(WiFi.channel(i));
      file.print(',');
      file.print(WiFi.RSSI(i)); 
      file.print(',');
      file.print(String(lat, 6));
      file.print(',');
      file.println(String(lng, 6));
      //file.close();
    }
    file.close();
    display.drawString(120, 29, String(lat, 6));
    display.drawString(120, 39, String(lng, 6));
    Serial.print("Position: ");
    Serial.print(lat, 6);
    Serial.print(" ");
    Serial.print(lng, 6);
    Serial.println();
  }
  display.display();
  display.clear();
}

void loop(){
  if (ss.available() > 0){
    if (gps.encode(ss.read())){
      Serial.print("Date/Time: ");
      Serial.print(gps.date.month());
      Serial.print(F("/"));
      Serial.print(gps.date.day());
      Serial.print(F("/"));
      Serial.print(gps.date.year());
      Serial.print(" ");
      if (gps.time.hour() < 10) Serial.print(F("0"));
      Serial.print(gps.time.hour());
      Serial.print(F(":"));
      if (gps.time.minute() < 10) Serial.print(F("0"));
      Serial.print(gps.time.minute());
      Serial.print(F(":"));
      if (gps.time.second() < 10) Serial.print(F("0"));
      Serial.print(gps.time.second());
      Serial.print(F("."));
      if (gps.time.centisecond() < 10) Serial.print(F("0"));
      Serial.print(gps.time.centisecond());
      Serial.println();
      lookForNetworks(gps.location.lat(), gps.location.lng());
    }
  }
  else{
    display.setFont(ArialMT_Plain_16);
    Serial.println("Finding Satellites");
    display.drawString(125, 30, "Finding Satellites");
    display.display();
    display.clear(); 
  }
}

void initializeSD() { // create new CSV file and add WiGLE headers
  int i = 0; 
  filename = "wifi0.csv";
  while (SD.exists(filename)) {
    i++; 
    filename = "wifi" + String(i) + ".csv";
  }
  File file = SD.open(filename, FILE_WRITE);
  if (file) {
    //file.println("MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,Latitude,Longitude,Type");
    file.println("MAC,SSID,AuthMode,Channel,RSSI,Latitude,Longitude");

  }
  file.close();
}

String getEncryption(uint8_t network, String src) { // return encryption for WiGLE or print
  byte encryption = WiFi.encryptionType(network);
  switch (encryption) {
    case 2:
      if (src=="screen") { return "WPA"; }
      return "[WPA-PSK-CCMP+TKIP][ESS]";
    case 5:
      if (src=="screen") { return "WEP"; }
      return "[WEP][ESS]";
    case 4:
      if (src=="screen") { return "WPA2"; }
      return "[WPA2-PSK-CCMP+TKIP][ESS]";
    case 7:
      if (src=="screen") { return "NONE" ; }
      return "[ESS]";
    case 8:
      if (src=="screen") { return "AUTO"; }
      return "[WPA-PSK-CCMP+TKIP][WPA2-PSK-CCMP+TKIP][ESS]";
  }
}
