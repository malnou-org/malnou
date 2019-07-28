# Configuration and Setup

## Parts and components required

* Raspberry pi 3/4
* Xaiomi scale 2
* Elechouse PN532 NFC module v3 / Adafruit PN532
* HC SR04 ultrasonic ranging module

## Breadboard diagram
![LISA](https://github.com/malnou-org/malnou/blob/master/L.I.S.A/Images/L.I.S.A.png)

**The NFC module we used for the prototype was Elechouse PN532 NFC Module v3.
The software used to make this diagram was Fritzing and they did'nt have a Elechouse module so an adafruit module was used for 
illustration purpose.**

## Configuration

* Install Raspbian OS on your Pi. Follow this [tutorial.](https://www.youtube.com/watch?v=RQ6JvnXwDCM)

* Connect the circuit as shown in the diagram

* Enable I2C interface on the Pi
  Run 
  ```bash
  sudo raspi-config
  ```
  Use the down arrow to select 5 Interfacing Options
  Arrow down to P5 I2C.
  Select yes when it asks you to enable I2C
  Also select yes if it asks about automatically loading the kernel module.
  Use the right arrow to select the <Finish> button.
  Select yes when it asks to reboot.
  
* Install libnfc and i2c-tools.
```bash
wget http://dl.bintray.com/nfc-tools/sources/libnfc-1.7.1.tar.bz2
tar -xf libnfc-1.7.1.tar.bz2 
cd libnfc-1.7.1/
./configure --prefix=/usr --sysconfdir=/etc
sudo make install
sudo apt-get install libusb-dev libpcsclite-dev i2c-tools
```
* Create device config file
```bash
sudo mkdir /etc/nfc
sudo nano /etc/nfc/libnfc.conf
```
* Inside the file write
```bash
# Allow device auto-detection (default: true)
# Note: if this auto-detection is disabled, user has to set manually a device
# configuration using file or environment variable
allow_autoscan = true

# Allow intrusive auto-detection (default: false)
# Warning: intrusive auto-detection can seriously disturb other devices
# This option is not recommended, user should prefer to add manually his device.
allow_intrusive_scan = false
```
* Now enable the 2 modules
```bash
sudo nano /etc/modules
```
* Inside the file write
```bash
# /etc/modules: kernel modules to load at boot time.
#
# This file contains the names of kernel modules that should be loaded
# at boot time, one per line. Lines beginning with "#" are ignored.

i2c-bcm2708
i2c-dev
```
* Reboot and type 
```bash 
sudo i2cdetect -y 1
```
If the outut looks like this then the i2c interface is properly setup on your raspberry pi
```bash
pi@raspberrypi:~ $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- 24 -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- -- 
```
* Set the selector switches on the nfc module to first up and second down as shown in the pic
![NFC](https://github.com/malnou-org/malnou/blob/master/L.I.S.A/Images/pn532.jpg)

This is to select the interfacing mode on the nfc chip 10 on the selector chip refers to i2c 

* Test the nfc module by typing
```bash
nfc-poll
```
Then swipe a nfc tag on the module to get the result like this if it is configured correctly.
```bash
pi@raspberrypi:~ $ nfc-poll 
nfc-poll uses libnfc 1.7.1
NFC reader: pn532_i2c:/dev/i2c-1 opened
NFC device will poll during 30000 ms (20 pollings of 300 ms for 5 modulations)
ISO/IEC 14443A (106 kbps) target:
    ATQA (SENS_RES): 00  04  
       UID (NFCID1): f4  8d  8a  ab  
      SAK (SEL_RES): 08  
nfc_initiator_target_is_present: Target Released
Waiting for card removing...done.
```
## Dependencies
To install all the dependencies type
```bash
pip install -r requirements.txt
```
