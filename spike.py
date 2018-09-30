import math


class Spike:

    # Конструктор
    # id - уникальный индификатор
    # strength - прочность колючки
    # power - сила колючки
    # x - координата по x
    # y - координата по y
    def __init__(self, id, strength, power, x, y):
        self.__id = id
        self.__strength = strength
        self.__power = power
        self.__x = x
        self.__y = y

    # Уменьшает прочность на заданную величину
    # delta - величина, на которую мы меняем прочность
    def change_strenght(self, delta):
        self.__strength = self.__strength + delta

        if self.__strength < 0:
            self.__strength = 0

    # Уменьшает силу на заданную величину
    # delta - величина, на которую мы меняем силу
    def change_power(self, delta):
        self.__power = self.__power + delta

        if self.__power < 0:
            self.__power = 0

    # Колючка бьет червяка
    # Уменьшает здоровье червяка и прочность колючки
    # worm - объект червяка
    def hit(self, worm):
        self.__strength = self.__strength - worm.get_power()
        self.__power = self.__power - math.sqrt(worm.get_power())

    # Присваивает заданную прочность
    def set_strenght(self, strenght):
        self.__strength = strenght

    # Присваивает заданную силу
    def set_power(self, power):
        self.__power = power

    # Возвращает id колючки
    def get_id(self):
        return self.__id

    # Возвращает прочность колючки
    def get_strength(self):
        return self.__strength

    # Возвращает силу колючки
    def get_power(self):
        return self.__power

    # Возвращает координату по x
    def get_x(self):
        return self.__x

    # Возвращает координату по y
    def get_y(self):
        return self.__y
