# d0raCarch - Wardriving device
Small and pocket-sized, a phrase that is completely misunderstood if taken out of context, I am talking about a Wardriving device.
<p align="center"><img src="/image/1.jpg"></p>

## For the creation of this project you will need:
- Wemos d1 mini
- sd module
- m6 gps module
- 128x64 display

## Pay attention
In the file WifiScan.ino you will find the instructions for the connections, pay special attention to the connection of the gps module: the rx pin is connected to pin D4(gpio 2) but in the .ino file the connection to pin D3(gpio 0) is indicated, same for the Tx pin, it is connected to pin D3(gpio 0) but the connection to pin D4(gpio 2) is indicated. Pay attention!

## Assembly
Below are some pictures of the device without a case, so that you can understand how to place the modules to optimise space.
<p align="center"><img src="/image/5.jpg"></p>
<p align="center"><img src="/image/6.jpg"></p>

## 3D Case
Finally, in the 3d folder you will find the two files for 3d printing of the case.
<p align="center"><img src="/image/7.png"></p>
<p align="center"><img src="/image/8.png"></p>
