#

class Animation(object):
    def __init__(self, neopixels, num_pixels):
        self.num_pixels = num_pixels
        self.neopixels = neopixels
        self.counter = 0
    
    def next_frame(self):
        pass