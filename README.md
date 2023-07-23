# RGB-OS
A circuitpython project for easily creating Neopixel devices.
Usage is simple: RGB-OS defines a series of patterns. These are classes, derived from `Animation()`.
Upon calling the function `next_frame()` the class will write the next frame to the neopixels (passed into the class upon `__init__()`)
The `main.py` file first makes a list of the animations, and starts playing the first one. If you press the button 
(defined in `main.py`), it stops playing the first animation, and moves on to the next. Pressing it again will play the third.

## Usage
To use, first install circuitpython on a microcontroller, and attatch neopixels. Then, erase all of the files on the
microcontroller, and replace with the files in this repo (even the `lib` folder). Then, open `main.py` in a text editor, 
and follow the steps detailed in the file.