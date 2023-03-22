# d0raCarch V1 - Wardriving device
<p align="center">
 <img alt="Arduino" src="https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white">
 <img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">
</p>

Small and pocket-sized, a phrase that is completely misunderstood if taken out of context, I am talking about a Wardriving device.
<p align="center"><img src="/image/1.jpg"></p>
<p align="center"><img src="/image/3.jpg"></p>

## For the creation of this project you will need:
- [Wemos d1 mini](https://www.amazon.it/AZDelivery-D1-ESP8266-12E-gratuito-compatibile/dp/B0754N794H/ref=sr_1_7?keywords=wemos+d1+mini&qid=1677771028&sprefix=wemos+d%2Caps%2C177&sr=8-7)
- [SD module](https://www.amazon.it/AZDelivery-Reader-Memory-Shield-Arduino/dp/B06X1DX5WS/ref=sr_1_5?keywords=arduino+sd+card+module&qid=1677771051&sprefix=sd+module+a%2Caps%2C164&sr=8-5)
- [M6 gps module](https://www.amazon.it/Aideepen-GY-GPS6MV2-Posizione-Antenna-Controller/dp/B08CZSL193/ref=sr_1_6?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1RTDJSP7UCFB8&keywords=gps+arduino&qid=1677771070&sprefix=gps+arduino%2Caps%2C163&sr=8-6)
- [Display 128x64](https://www.amazon.it/gp/product/B07J2QWF43/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

## Pay attention
In the file WifiScan.ino you will find the instructions for the connections, pay special attention to the connection of the gps module: the rx pin is connected to pin D4(gpio 2) but in the .ino file the connection to pin D3(gpio 0) is indicated, same for the Tx pin, it is connected to pin D3(gpio 0) but the connection to pin D4(gpio 2) is indicated. 

Remember, after connected all pin and completed the assembly you should go out and power on the device, after 5/10 minutes if all connection is ok the gps should blink.
Pay attention!

## How it works
It essentially scans the networks around you via the Wemos, obtains the position via the GPS and stores them in .csv format on an sd card.

To drop duplicates you should use the file main.py into Advance folder, this script can:
- Get all file to merge from ToMerge folder, check and drop all duplicates row and save the final result into Done folder.
- Get the file to clean from ToClean folder, check and drop all duplicates and save the final result into Done folder.
- Generate and save the 2D Map into Map folder.

<p align="center"><img src="/image/map.gif"></p>

## Assembly
Below are some pictures of the device without a case, so that you can understand how to place the modules to optimise space.
<p align="center"><img src="/image/5.jpg"></p>
<p align="center"><img src="/image/6.jpg"></p>

## 3D Case
Finally, in the 3D/Version1 folder you will find the two files for 3d printing of the case.
<p align="center"><img src="/image/7.png"></p>
<p align="center"><img src="/image/8.png"></p>

# d0raCatch V2
<p align="center"><img src="/image/7.jpg"></p>

## For the creation of this project you will need:
- [Battery](https://www.amazon.it/dp/B0B7N2T1TD?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [Antenna](https://www.amazon.it/dp/B09NXZ35CM?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [Connector](https://www.amazon.it/dp/B07YBYMBSV?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [Battery Charger](https://www.amazon.it/dp/B0B17R8CMG?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [Switch](https://www.amazon.it/dp/B09QQLTQ1C?psc=1&ref=ppx_yo2ov_dt_b_product_details)

## 3D Case
Finally, in the 3D/Version2 folder you will find the two files for 3d printing of the case.
<p align="center"><img src="/image/9.png" width="1000" height="720"></p>
<p align="center"><img src="/image/10.png" width="1000" height="720"></p>

## Disclaimer
I recommend using this device for testing, learning and fun :D
