FTC_Arcade_Pay
==============

Python code to use a Raspbery Pi as a feathercoin payment device for arcade machines
Required libraries are
required, requests, setup,Pillow, QRcode
Quick install of modules is
sudo apt-get install python-dev python-setuptools libjpeg-dev zlib1g-dev libpng12-dev libfreetype6-dev
sudo apt-get install python-pip
sudo apt-get remove Pil
sudo pip install Pillow
plus QRcode from
https://pypi.python.org/pypi/qrcode
The intent of this software is to allow a Raspbery Pi to be used as a payment device for arcade machine for Feathercoin using the API call hosted on the Feathercoin website
https://www.feathercoin.com/feathercoin-api/

Cost per credit can be set as a static FTC price, or any value in any currency supported by the Feathercoin API and on start it will covert this to the closest whole FTC to be used as the credit price

Required hardware is a Raspberry Pi Model B plus the Adafruit PiTFT Mini Kit - 320x240 2.8" TFT+Touchscreen which can be purcahsed from here
https://www.adafruit.com/products/1601

Once the display has been assembled and instaleld follow ADafruits setup instructions here
https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi
Make sure you install fbi as per the instructions above to display the PNG images

Output to the relay will be via pin 16 on the GPIO, ensure you use an appropriate cct to drive the realy

On startup is the credit price is set by a Fiat it will first look up the API to convert this to FTC.
It will then create a QR code based on this price, your feathercoin wallet price which is set in main.py and your text message to appear in the wallets.
It will then add this to a larger background image, add in the featehrcoin logo and text detailing the cost per credit and produce qr.png.
this will then be displayed on the screen to be scanned.

Every 15 seconds it polls the API to see if a credit has been purchased, if it can't contact the API the QR code is removed an a offline iamge is displayed to stop people sending FTC when the machine is offline.

More than 1 credit can be purchased at a time, it simply counts off the credit to the relay.
Timing of how long the relay is to be activated will depend on the device you are connecting this to.

You will need to create an PNG file called CSN.png to be displayed when your Raspberry Pi can't talk to the API, no larger than 320x240

If you like it feel free to send a donation to 6ihSh7xDnnwLJqKVAKZetTqzttxbSrnaLJ  FTC
