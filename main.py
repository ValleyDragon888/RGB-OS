import board
import digitalio
import time
import neopixel

# import animations
from colourchase import ColourChase
from SoftFade import SoftFade
from GentleGlow import GentleGlow
from SingleChase import SingleChase

# init neopixels and button
num_pixels = 50
pixels = neopixel.NeoPixel(board.GP0, num_pixels)
pixels.brightness = 0.5

button = digitalio.DigitalInOut(board.GP1)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# make an instance of each animaton
animations = [
        ColourChase(pixels, num_pixels),
        SoftFade(pixels, num_pixels),
        GentleGlow(pixels, num_pixels),
        SingleChase(pixels, num_pixels)
    ]
num = 0

def button_is_pressed():
    return button.value


while True:
    if button.value:
        #print("next anim")
        num += 1
        if num > len(animations)-1:
            #print(f"bak to start {num}")
            num = 0
        time.sleep(1)
    animations[num].next_frame()#33:33 linenum:charnum!
