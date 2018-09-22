import math


class Spike:

    # Конструктор
    # strength - прочность колючки
    # power - сила колючки
    def __init__(self, strength, power):
        self.strength = strength
        self.power = power

    # Колючка бьет червяка
    # Уменьшает здоровье червяка и прочность колючки
    # worm - объект червяка
    def hit(self, worm):
        self.strength = self.strength - worm.get_power()
        self.power = self.power - math.sqrt(worm.get_power())
        worm.set_life(worm.get_life() - self.strength)

    # Возвращает прочность колючки
    def get_strength(self):
        return self.strength

    # Возвращает силу колючки
    def get_power(self):
        return self.power

    # Присваивает заданную прочность
    def set_strenght(self, strenght):
        self.strength = strenght

    # Присваивает заданную силу
    def set_power(self, power):
        self.power = power

    # Уменьшает прочность на заданную величину
    # delta - величина, на которую мы меняем прочность
    def change_strenght(self, delta):
        self.strength = self.strength + delta

        if self.strength < 0:
            self.strength = 0

    # Уменьшает силу на заданную величину
    # delta - величина, на которую мы меняем силу
    def change_power(self, delta):
        self.power = self.power + delta

        if self.power < 0:
            self.power = 0
