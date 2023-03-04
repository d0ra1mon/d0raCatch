 # d0raCarch - Wardriving device
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

Small and pocket-sized, a phrase that is completely misunderstood if taken out of context, I am talking about a Wardriving device.
<p align="center"><img src="/image/1.jpg"></p>
<p align="center"><img src="/image/3.jpg"></p>

## For the creation of this project you will need:
- [Wemos d1 mini](https://www.amazon.it/AZDelivery-D1-ESP8266-12E-gratuito-compatibile/dp/B0754N794H/ref=sr_1_7?keywords=wemos+d1+mini&qid=1677771028&sprefix=wemos+d%2Caps%2C177&sr=8-7)
- [SD module](https://www.amazon.it/AZDelivery-Reader-Memory-Shield-Arduino/dp/B06X1DX5WS/ref=sr_1_5?keywords=arduino+sd+card+module&qid=1677771051&sprefix=sd+module+a%2Caps%2C164&sr=8-5)
- [M6 gps module](https://www.amazon.it/Aideepen-GY-GPS6MV2-Posizione-Antenna-Controller/dp/B08CZSL193/ref=sr_1_6?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1RTDJSP7UCFB8&keywords=gps+arduino&qid=1677771070&sprefix=gps+arduino%2Caps%2C163&sr=8-6)
- [Display 128x64](https://www.amazon.it/gp/product/B07J2QWF43/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

## Pay attention
In the file WifiScan.ino you will find the instructions for the connections, pay special attention to the connection of the gps module: the rx pin is connected to pin D4(gpio 2) but in the .ino file the connection to pin D3(gpio 0) is indicated, same for the Tx pin, it is connected to pin D3(gpio 0) but the connection to pin D4(gpio 2) is indicated. Pay attention!

## How it works
It essentially scans the networks around you via the Wemos, obtains the position via the GPS and stores them in .csv format on an sd card.
Please note that it does not check for duplicates so you will have to remove them later via a python script. In order to be able to view the 2d map of the networks found, you should use this site: [Map](https://www.gpsvisualizer.com/)
<p align="center"><img src="/image/map.gif"></p>

## Assembly
Below are some pictures of the device without a case, so that you can understand how to place the modules to optimise space.
<p align="center"><img src="/image/5.jpg"></p>
<p align="center"><img src="/image/6.jpg"></p>

## 3D Case
Finally, in the 3D folder you will find the two files for 3d printing of the case.
<p align="center"><img src="/image/7.png"></p>
<p align="center"><img src="/image/8.png"></p>

## Disclaimer
I recommend using this device for testing, learning and fun :D
