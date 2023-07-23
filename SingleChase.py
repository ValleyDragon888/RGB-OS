#

from van_animation_base_class import Animation
import time

class SingleChase(Animation):
    def __init__(self, neopixels, num_pixels):
        super().__init__(neopixels, num_pixels)
        self.colours = [(225, 0, 0), (0, 225, 0), (0, 0, 225), (0, 112, 112), (112, 112, 0), (112, 0, 112), (150, 75, 0), (0, 75, 150),
                        (0, 150, 75), (75, 150, 0), (150, 0, 75)]
        self.current_col = 0
        self.counter += 1
    
    def next_frame(self):
        if self.counter > self.num_pixels:
            self.counter = 1
            self.current_col += 1
            if self.current_col > len(self.colours)-1:
                self.current_col = 0
        
        self.neopixels.fill((0, 0, 0))
        self.neopixels[self.counter-1] = self.colours[self.current_col]
        #print(self.neopixels)
        self.counter += 1
        self.neopixels.show()
        time.sleep(0.1)
