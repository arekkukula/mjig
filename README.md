# mjig

Raspberry Pico based mouse jiggler, built on _CircuitPython_.

The cursor moves every 10 seconds to keep your computer running.\
Support for toggling it on/off by a press of a button.

Tested and working on Windows, MacOS.

While plugged in, it's recognized as a HID mouse device, unless special conditions
are met (see [special conditions](#special-conditions)).
_____
## Configuration
To change the default behavior, see file **config.py**.\
In this file you can easily set the following:
- interval between mouse movements,
- maximum X and Y values by which the mouse moves,
- if the jiggler should be enabled on start.
_____
## Installation
1. download .UF2 file containing CircuitPython (https://circuitpython.org/board/raspberry_pi_pico/) and follow instructions.
2. Install `adafruit_hid` (https://github.com/adafruit/Adafruit_CircuitPython_HID) module in your Pico's */lib* folder.
3. After installation succeeded, drag and drop all `.py` files from this repo into the root catalog of your Pico.

That's it!

_____
## Build
![Schema](/docs/schema.png)

### __Bare minimum (no LED activity):__
- Nothing! Just plug your Raspberry Pico to PC, mjig is active by default.

### __Full build:__
- 1 push button
- 1 LED
- 2 resistors

Connect the push button to __GP15__ and ground through a resistor. Allows to toggle the jiggler on/off.\
Connect the LED to __GP12__ and ground through a resistor. The LED indicates, whether the jiggler is enabled or not.

_____
## Special Conditions
While using _CircuitPython_, Pico's mass storage is enabled by default,
and a window pops up everytime Pico's plugged in. \
To avoid that, the mass storage is disabled on boot.\
\
If you're stuck and want to access the storage, you can either:
- Ground GP0 before connecting the Pico to PC,
- Press the switch connected to GP15 while plugging Pico to PC.

_____
## Disclaimer
The contents of this repository are provided "AS IS".\
By using any part of this repository (code, instructions, etc.), you agree that you do it at your own risk.\
You acknowledge that working with electrical devices is hazardous, and that they should be handled cautiously and with no negligence.\
I am not responsible for any damage to the equipment or injuries.