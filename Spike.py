class Spike:
    def __init__(self, id, x, y, strength=100, power=100):
        self.__id = id
        self.__strength = strength
        self.__power = power
        self.__time = 0
        self.__x = x
        self.__y = y
    
    def tick(self):
        self.__time += 1
    
    def reduce_strenght(self, delta):
        self.__strength -= delta

        if self.__strength < 0:
            self.__strength = 0
    
    def change_power(self, delta):
        self.__power = self.__power + delta

        if self.__power < 0:
            self.__power = 0
    
    def set_strenght(self, strenght):
        self.__strength = strenght
    
    def set_power(self, power):
        self.__power = power
    
    def get_time(self):
        return self.get_time()
    
    def get_id(self):
        return self.__id
    
    def get_strength(self):
        return self.__strength
    
    def get_power(self):
        return self.__power
    
    def get_position(self):
        return (self.__x, self.__y)

