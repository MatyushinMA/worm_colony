class Thread:

    # Конструктор
    # worms_list - список из объектов червей
    # spikes_list - список из объектов колючек
    # foods_list - список из объектов еды
    # width - ширина среды
    # length - длина среды
    def __init__(self, worms_list, spikes_list, foods_list, width, length):
        self.__worms_list = worms_list
        self.__spikes_list = spikes_list
        self.__foods_list = foods_list
        self.__width = width
        self.__length = length

    # Добавить в среду червя
    # worm - объект червя
    def set_worm(self, worm):
        self.__worms_list.add(worm)

    # Добавить в среду колючку
    # spike - объект колючки
    def set_spike(self, spike):
        self.__spikes_list.add(spike)

    # Удаляет червяка по id
    # id - индификатор червяка
    def delete_worm(self, id):
        for worm in enumerate(self.__worms_list):
            if worm[1].get_id() == id:
                del self.__worms_list[worm[0]]
        return None

    # Удаляет еду по id
    # id - индификатор еды
    def delete_food(self, id):
        for food in enumerate(self.__foods_list):
            if food[1].get_id() == id:
                del self.__spikes_list[food[0]]
        return None

    # Удаляет колючку по id
    # id - индификатор колючки
    def delete_spike(self, id):
        for spike in enumerate(self.__spikes_list):
            if spike[1].get_id() == id:
                del self.__spikes_list[spike[0]]
        return None

    # Возвращает червя по id
    def get_worm(self, id):
        for worm in self.__worms_list:
            if worm.get_id() == id:
                return worm
        return None

    # Возвращает список червей
    def get_worms(self):
        return self.__worms_list

    # Возвращает еду по id
    def get_food(self, id):
        for food in self.__foods_list:
            if food.get_id() == id:
                return food
        return None

    # Возвращает список еды
    def get_foods(self):
        return self.__foods_list

    # Возвращает колючку по id
    def get_spike(self, id):
        for spike in self.__spikes_list:
            if spike.get_id() == id:
                return spike
        return None

    # Возвращает список колючек
    def get_spikes(self):
        return self.__spikes_list
