class Food:

    # Конструктор
    # saturation - сытость еды (чем еда сытнее, тем больше здоровья дает червяку)
    # time - время до того момента, как закончится "срок годности" еды
    # spoiled - является ли еда испорченной
    # Еда становится испроченной, как только обнуляется переменная time
    # Испорченная еда наносит вред червяку
    def __init__(self, saturation, time):
        self.saturation = saturation
        self.time = time
        self.spoiled = False

    # Возвращает сытость еды
    def get_saturation(self):
        return self.saturation

    # Возвращает количество времени, до того как еда испортится
    def get_time(self):
        return self.time

    # Возвращает, является ли еда испорченной или нет
    # True - испорченна
    # False - не испорченна
    def get_spoiled(self):
        return self.spoiled

    # Присваивает заданную сытость
    def set_saturation(self, saturation):
        self.saturation = saturation

    # Уменьшает время на заданную величину
    # delta - величина, на которую мы меняем время
    def tik(self, period):
        self.time = self.time - period

        if self.time <= 0:
            self.spoiled = True
            self.time = 0
