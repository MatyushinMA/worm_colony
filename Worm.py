import Nnet

class Worm:
    def __init__(self, id, x, y):
        self.id = id
        self.health = 100
        self.time = 0
        self.power = 1
        self.saturation = 100
        
        self.net = WormNET()
        self.x = x
        self.y = y
    
    def next_action(self, env):
        self.time += 1
        pred = self.net(env)
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
        return (self.x_coordinate, self.y_coordinate)
    
    def set_position(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
