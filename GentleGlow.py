#
# practicslly doesnt do anything so dosnt deed to inherit Animation

class GentleGlow(object):
    def __init__(self, pixels, num_pixels):
        self.pixels = pixels
    
    def next_frame(self):
        self.pixels.fill((100, 100, 100))