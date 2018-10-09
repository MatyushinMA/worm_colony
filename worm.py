
class Worm: # класс червяка
    # health - здоровье
    # power - сила
    # saturation - сытость 
    # time - время жизни
    # TODO: выставиь начальные значения power, saturation
    def __init__(self, health, path_to_xml, x_coordinate, y_coordinate):
        self.health=health 
        self.time=0
        self.net=WormNET(path_to_xml)
        self.power=1
        self.saturation=1
        self.x_coordinate=x_coordinate
        self.y_coordinate=y_coordinate
        
    # Функция принятия решения о последующем действии
    # сначала проверяем, жив ли червяк
    # спрашиваем у НС что нам делать
    # прибавляем себе единицу жизни
    # вызываем выбранную функцию взаимодействия из другого класса
    def next_action(self, x):
        pred=self.net.feed(x)
        self.time=self.time+1
        #Здесь вызываем нужную функцию класса "среда" 
        #в зависимости от решения червяка
        pass
    
    # возвращает силу червяка
    def get_power(self):
        return self.power
    
    # присваивает силу червяка
    def set_power(self, p):
        self.power=p
        
    # возвращает здоровье 
    def get_health(self):
        return self.health
    
    # присваивает здоровье
    def set_health(self, h):
        self.health=h
    
    # возвращает сытость
    def get_saturation(self):
        return self.saturation
    
    # присваивает сытость
    def set_saturation(self, s):
        self.saturation=s
        
    # возвращает текущий возраст червяка    
    def get_time(self):
        return self.time 
    
    # создает х - "вход" для нейронной сети
    def create_x(self, x):
        #TODO!!!
        pass

