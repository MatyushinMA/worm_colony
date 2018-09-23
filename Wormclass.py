class Worm: # класс червяка
    # health - здоровье
    # power - сила
    # saturation - сытость 
    # time - время жизни
    def __init__(health, max_power, max_time, path_to_xml):
        self.health=health 
        self.time=0
        self.net=WormNET(path_to_xml)
        self.power=1
        self.max_power=max_power
        self.max_time=max_time
        self.saturation=1
        
    # Функция принятия решения о последующем действии
    # сначала проверяем, жив ли червяк
    # спрашиваем у НС что нам делать
    # прибавляем себе единицу жизни
    # вызываем выбранную функцию взаимодействия из другого класса
    def next_action(self, x):
        if self.time > self.max_time :
            self.health=0 
            return -1
        if self.saturation <= 0 :
            self.health=0 
            return -1
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
       

