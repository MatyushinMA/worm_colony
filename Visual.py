import cv2
import numpy as np

from Utils import *

class Visual:
    def __init__(self, params):
        self.params = params
    
    def show_positions(self, colony, environment):
        width = self.params['world_width']*self.params['width_scale']
        height = self.params['world_height']*self.params['height_scale']
        frame = np.zeros((width, height, 3), np.uint8)
        for w in colony:
            worm_position = w.get_position()
            worm_x, worm_y = worm_position[0], worm_position[1]
            x1 = worm_x*self.params['width_scale']
            x2 = (worm_x+1)*self.params['width_scale']
            y1 = worm_y*self.params['height_scale']
            y2 = (worm_y+1)*self.params['height_scale']
            cv2.rectangle(frame, (x1, y1), (x2, y2), self.params['draw_color'], 3)
            cv2.imshow('Visual', frame)
            cv2.waitKey(100)
    
    def clear(self):
        cv2.destroyAllWindows()
