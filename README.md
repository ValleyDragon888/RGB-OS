# RGB-OS
A circuitpython project for easily creating Neopixel devices.
Usage is simple: RGB-OS defines a series of patterns. These are classes, derived from `Animation()`.
Upon calling the function `next_frame()` the class will write the next frame to the neopixels (passed into the class upon `__init__()`)
The `main.py` file first makes a list of the animations, and starts playing the first one. If you press the button 
(defined in `main.py`), it stops playing the first animation, and moves on to the next. Pressing it again will play the third.
If you diddn't understand that, don't worry. Move on to the usage section below, for how to get started.

## Usage
To use, first install circuitpython on a microcontroller, and attatch neopixels. Then, erase all of the files on the
microcontroller, and replace with the files in this repo (even the `lib` folder). Then, open `main.py` in a text editor, 
and follow the steps detailed in the file. (It's super easy!!)

After that, should have changed everything necesarry to make it work!

## Contributing
### New features
If you have made changes to the program for your own use, that makes it better, please put it in a pull request!
It is relatively easy to make new animations - look at the animations in the patterns folder. If you make any, please Pull Request them!

### Bugs or Spelling Mistakes
If there are, heavens forbid, any bugs, spelling mistakes, missing bits of documentation, or problems with documentation,
please put it in an issue, or, fix it yourself and put it in a Pull Request!