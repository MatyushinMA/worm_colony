import random as rand


class Colony:
    # инициализация
    # задаем max_power, max_time
    def __init__(self, start_count_worm, max_worm, health, max_power, max_time, path_to_xml):
        self.max_worm=max_worm
        self.actual_worm=start_count_worm
        self.worm=[]
        self.max_power=max_power
        self.max_time=max_time
        for i in range(1, start_worm+1):
            # TODO: задание начального положения червя
            # x_coordinate=rand.randint(-100,100)
            # y_coordinate=rand.randint(-100,100)
            self.worm.append(Worm(health, path_to_xml, x_coordinate, y_coordinate))
    
    # убирает из списка погибших червей
    # возврашает число погибших червей
    def kill(self):
        count = 0 # количество погибших червей за 1 итерацию 
        for i in range(0, len(self.worm)):
            if self.worm[i].time > self.max_time or self.worm[i].saturation <= 0:
                self.worm[i].health=0   
            if self.worm[i].health == 0:
                self.worm.pop(i)
                count = count + 1        
        return count
    
    # один проход: червяк совершает действие, после чего происходит "чистка"
    # если вся колония погибла - ERROR
    def iteration(self):
        for i in range(0, len(self.worm)): 
            self.worm[i].create_x(x)
            self.worm[i].next_action(x)
        self.kill()
        if len(self.worm) <= 0:
            print ("Error, all worms are died !")
            return -1
        return 0
    
    # добваление червя с заданными параметрами
    def add_worm(self, health, path_to_xml, x_coordinate, y_coordinat):
        self.worm.append(Worm(health, path_to_xml, x_coordinate, y_coordinate))   

    # добавление червя с рандомными параметрами в пределах min и max
    def add_worm_random(self, path_to_xml):
        health=rand.randint(1,10)
        x_coordinate=rand.randinat(-100,100)
        y_coordinate=rand.randint(-100,100)
        self.worm.append(Worm(health, path_to_xml, x_coordinate, y_coordinate))  
        
    def get_count_of_worm(self): 
        return len(self.worm)
        
        
        

