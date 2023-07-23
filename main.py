# Welcome to the main.py file. Here are the steps necessary to get RGB OS up and running
# Just jump your eyes over the imports. (To JUMP TO HERE)
# Also please read the README.md before doing this.

import board
import digitalio
import time
import neopixel

# import animations
from patterns.colourchase import ColourChase
from patterns.SoftFade import SoftFade
from patterns.GentleGlow import GentleGlow
from patterns.SingleChase import SingleChase

# --------------------------JUMP TO HERE-------------------------
# First, edit these variables to your needs:
# This one is fairy self-explanitory. Input the number of neopixels you have.
num_pixels = 50
# Next, edit 'GP0' to the GPIO pin that the data pin of your neopixels are connected to.
pixels = neopixel.NeoPixel(board.GP0, num_pixels)
# If you find it's a problem, you cn change this: (0-1)
pixels.brightness = 0.5

# Now, the button is used to switch between different animations.
# On the next line, change 'GP1' to the gpio pin your button is connected to,
button = digitalio.DigitalInOut(board.GP1)
button.direction = digitalio.Direction.INPUT
# If your button is connected to power, don't change anything on the next bit of code.
# However, if you have connected it to ground, change 'DOWN' to 'UP'
button.pull = digitalio.Pull.DOWN

# Here is the list of animations, that you flip between by pressing the button
# If you would not like your device to use a certian animation, just remove the line.
# (To work out which one to remove, work out how many times you have to press the button get to it from switchon.)

animations = [
        ColourChase(pixels, num_pixels),
        SoftFade(pixels, num_pixels),
        GentleGlow(pixels, num_pixels),
        SingleChase(pixels, num_pixels)
    ]

# -----------------------END OF EDITABLE SECTION--------------------------

num = 0

def button_is_pressed():
    return button.value


while True:
    if button.value:
        num += 1
        if num > len(animations)-1:
            num = 0
        time.sleep(1)
    animations[num].next_frame()
