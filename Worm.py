from Nnet import WormNET
import torch

class Worm:
    def __init__(self, id, x, y, orientation=0):
        self.id = id
        self.health = 100
        self.time = 0
        self.power = 1
        self.saturation = 100
        self.orient = orientation
        
        self.net = WormNET()
        self.x = x
        self.y = y
    
    def __call__(self, env):
        self.time += 1
        feed_env = torch.from_numpy(env)
        feed_env = feed_env.permute(2, 0, 1)
        feed_env = feed_env.view(1, 3, 11, 12)
        feed_env = feed_env.float()
        pred = self.net(feed_env)
        return pred
    
    def get_id(self):
        return self.id
    
    def get_power(self):
        return self.power
    
    def set_power(self, p):
        self.power = p
    
    def get_health(self):
        return self.health
    
    def set_health(self, h):
        self.health = h
    
    def get_saturation(self):
        return self.saturation
    
    def set_saturation(self, s):
        self.saturation = s
    
    def get_time(self):
        return self.time
    
    def tick(self):
        self.time += 1

    def get_position(self):
        return (self.x, self.y, self.orient)
    
    def set_position(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orient = orientation
