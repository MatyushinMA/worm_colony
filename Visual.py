import cv2
import numpy as np

from Utils import *

from Food import Food
from Spike import Spike
from Worm import Worm

class Visual:
    def __init__(self, params):
        self.params = params
    
    def show_positions(self, colony, environment):
        width = self.params['world_width']*self.params['width_scale']
        height = self.params['world_height']*self.params['height_scale']
        frame = np.zeros((width, height, 3), np.uint8)
        for w in colony:
            worm_position = w.get_position()
            worm_x, worm_y = worm_position[:2]
            x1 = worm_x*self.params['width_scale']
            x2 = (worm_x+1)*self.params['width_scale']
            y1 = worm_y*self.params['height_scale']
            y2 = (worm_y+1)*self.params['height_scale']
            cv2.rectangle(frame, (x1, y1), (x2, y2), self.params['worm_draw_color'], 3)
        for el in environment:
            el_position = el.get_position()
            el_x, el_y = el_position[:2]
            x1 = el_x*self.params['width_scale']
            x2 = (el_x+1)*self.params['width_scale']
            y1 = el_y*self.params['height_scale']
            y2 = (el_y+1)*self.params['height_scale']
            draw_color = self.params['spike_draw_color']
            if isinstance(el, Food):
                draw_color = self.params['food_draw_color']
            cv2.rectangle(frame, (x1, y1), (x2, y2), draw_color, 3)
        cv2.imshow('Visual', frame)
        cv2.waitKey(100)
    
    def clear(self):
        cv2.destroyAllWindows()
