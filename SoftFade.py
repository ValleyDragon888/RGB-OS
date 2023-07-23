#

from animation_base_class import Animation
import time

class SoftFade(Animation):
    def __init__(self, neopixels, num_pixels):
        super().__init__(neopixels, num_pixels)
        self.colours = ["RED", "GREEN", "BLUE", "TURQUOISE"]
        self.current_col = 0
        self.counter += 1
        self.fade_direction = "brighter" # or "darker"
        self.current_brightness = 1
    
    def next_frame(self):
        if self.current_brightness == 225:
            self.fade_direction = "darker"
        elif self.current_brightness == 0:
            self.fade_direction = "brighter"
            self.current_col += 1
            if self.current_col > len(self.colours)-1:
                self.current_col = 0
            
        
        if self.fade_direction == "darker":
            self.current_brightness -= 1
        else:
            self.current_brightness += 1
        
        if self.current_col == 0:
            self.neopixels.fill((self.current_brightness, 0, 0))
        elif self.current_col == 1:
            self.neopixels.fill((0, self.current_brightness, 0))
        elif self.current_col == 2:
            self.neopixels.fill((0, 0, self.current_brightness))
        elif self.current_col == 3:
            self.neopixels.fill((0, self.current_brightness, self.current_brightness))
        
        



