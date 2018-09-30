class Food:

    # Конструктор
    # id - уникальный индификатор
    # saturation - сытость еды (чем еда сытнее, тем больше здоровья дает червяку)
    # time - время до того момента, как закончится "срок годности" еды и она исчезнет
    # spoiled - является ли еда испорченной
    # x - координата еды по x
    # y - координата еды по y
    # Еда становится испроченной, как только обнуляется переменная time
    # Испорченная еда наносит вред червяку
    def __init__(self, id, saturation, time, x, y):
        self.__id = id
        self.__saturation = saturation
        self.__time = time
        self.__x = x
        self.__y = y

    # Уменьшает время на заданную величину
    # delta - величина, на которую мы меняем время
    def tik(self, period):
        self.__time = self.__time - period
        if self.__time <= 0:
            self.__time = 0

    # Уменьшает сытость на заданную величину
    # delta - величина, на которую мы меняем сытость
    def change_saturation(self, delta):
        self.__saturation = self.__saturation - delta

        if self.__saturation <= 0:
            self.__saturation = 0

    # Присваивает заданную сытость
    def set_saturation(self, saturation):
        self.__saturation = saturation

    # Возвращает id колючки
    def get_id(self):
        return self.__id

    # Возвращает сытость еды
    def get_saturation(self):
        return self.__saturation

    # Возвращает количество времени, до того как еда испортится
    def get_time(self):
        return self.__time

    # Возвращает координату по x
    def get_x(self):
        return self.__x

    # Возвращает координату по y
    def get_y(self):
        return self.__y
