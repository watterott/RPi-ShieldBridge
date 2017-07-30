# MI0283QT-Adapter v1

There is a [Linux Framebuffer driver (FBTFT)](https://github.com/notro/fbtft) available for the display adapter with MI0283QT-2 (HX8347D) + MI0283QT-9 / -11 (ILI9341) display panel and the ADS7846 / TSC2046 touch controller has also a Linux device driver.

An installation guide can be found [here](https://github.com/watterott/RPi-Display/blob/master/docs/FBTFT-Install.md).

It is also possible to use the ready to run [SD-Card image for the RPi-Display](https://github.com/watterott/RPi-Display) with modified parameters.
The respective parameters can be found in the installation guide under *FBTFT Kernel Modules*.

**Further Infos/Tutorials**
* [MI0283QT9 + RPi-ShieldBridge](http://lallafa.de/blog/2013/07/watterotts-new-rpi-shieldbridge/)
* [MI0283QT9 + RPi-ShieldBridge (German)](http://www.mdtweb.de/index.php/projekte/mikroprozessoren/raspberry-pi/rpi-lcd-ansteuerung)
* [MI0283QT9 + RPi-ShieldBridge (German)](http://www.forum-raspberrypi.de/Thread-tutorial-watterott-mi0283qt-9a-am-pi-betreiben)
* [MI0283QT9 driver installation](http://lallafa.de/blog/2013/03/watterott-mi0283qt-9a-display-for-the-rasbperry-pi/)
* [MI0283QT2 driver installation](http://lallafa.de/blog/2013/03/watterott-display-on-raspberry-pi/)
* [ADS7846 driver installation](http://lallafa.de/blog/2013/03/adding-touch-support-for-the-mi0283qt-displays/)
* [MI0283QT9 and BeagleBone Black](https://github.com/notro/fbtft/wiki/BeagleBone-Black)

**Display Connection**
```
Display  Raspberry Pi
---------------------
LCD-LED  GPIO24
LCD-RST  GPIO23
LCD-CS   GPIO8  (CE0) [on RPi-ShieldBridge v1.0: CE1]
ADS-CS   GPIO7  (CE1) [on RPi-ShieldBridge v1.0: CE0]
ADS-IRQ  GPIO25 (close Jumper JIRQ, open Jumper JSDA+JSCL)
MISO     GPIO9  (MISO)
MOSI     GPIO10 (MOSI)
SCK      GPIO11 (SCK)
```


# MI0283QT-Adapter v2

There is an experimental [Linux Framebuffer driver (fbtft)](https://github.com/notro/fbtft) available for the display adapter v2 with ARM controller.

An installation guide can be found [here](https://github.com/watterott/RPi-Display/blob/master/docs/FBTFT-Install.md).

It is also possible to use the ready to run [SD-Card image for the RPi-Display](https://github.com/watterott/RPi-Display) with modified parameters.
The respective parameters can be found in the installation guide under *FBTFT Kernel Modules*.

**Display Connection**
```
Display  Raspberry Pi
---------------------
LCD-RST  GPIO23
LCD-CS   GPIO8  (CE0) [on RPi-ShieldBridge v1.0: CE1]
 --- SPI/SSI ---
MISO     GPIO9  (MISO)
MOSI     GPIO10 (MOSI)
SCK      GPIO11 (SCK)
 --- I2C ---
LCD-SDA  GPIO2  (SDA, close Jumper JSDA)
LCD-SCL  GPIO3  (SCL, close Jumper JSCL, open Jumper JIRQ)
```

*Note: The Raspberry Pi hardware revision 1 boards connect I2C bus 0 (GPIO 0 + 1) and revision 2 boards connect I2C bus 1 (GPIO 2 + 3) to the GPIO connector.*
