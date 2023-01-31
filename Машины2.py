import doctest


class Auto:
    def __init__(self, mark: str, release_year: int):
        """
            Создание и подготовка к работе объекта "Автомабили"
            :param mark: Марка автомобиля
            :param release_year: Дата выпуска авто
            Примеры:
        >>> auto = Auto("Лада", 2000)  # инициализация экземпляра класса
        """

        if not isinstance(mark, str):
            raise TypeError("Марка машины должна быть типа int")
        self.mark = mark
        if not isinstance(release_year, int):
            raise TypeError("Дата выпуска машины должна быть типа int")
        self.release_year = release_year

    def car_can_drive(self):
        return f"Автомобиль марки {self.mark} может ездить"

    def __str__(self):
        return f"Автомобиль марки {self.mark} был выпущен в {self.release_year}"

    def __repr__(self):
        return f"{self.__class__.__name__}(mark={self.mark!r}, release_year={self.release_year!r})"


class PassengerAuto(Auto):
    max_num_pass = 4

    def __init__(self, mark: str, release_year: int, max_speed: float):
        super().__init__(mark=mark, release_year=release_year)
        """ 
            Создание и подготовка к работе дочернего класса "Легковой авомобиль"
            В дочернем классе появляется новый параметр 
            :param max_speed: Максимальная скорость авто, км/ч
            Примеры:
        >>> p = PassengerAuto("Audi", 2010, 320)  # инициализация экземпляра класса
        """
        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть типа float")
        if max_speed < 0:
            raise ValueError("Максимальная скорость не может быть меньше нуля")
        self.max_speed = max_speed

    def num_of_pass(self, current_num_of_pass):
        """"
               Метод, который вычисляет, войдут ли все в автомобиль
               :param current_num_of_pass: количество пассажиров на данный момент
               max_num_pass: максимальное количество пассажиров в любой легковой машине по умолчанию
               :raise ValueError: Если current_num_of_pass будет больше max_num_pass
               Примеры:
                 Примеры:
        >>> p = PassengerAuto("Kamri", 2010, 150)
        >>> p.num_of_pass(1)
        """
        if not isinstance(current_num_of_pass, int):
            raise TypeError("Кол-во пассажиров должно быть типа float")
        if current_num_of_pass < 0:
            raise ValueError("Кол-во пассажиров не может быть меньше нуля")
        if current_num_of_pass > self.max_num_pass:
            raise ValueError("Кол-во пассажиров не должно превыщать 4 человек")

    def __str__(self):
        return f"Автомобиль марки {self.mark} был выпущен в {self.release_year}, максимальная скорость {self.max_speed}"

    def __repr__(self):
        return f"{self.__class__.__name__}(mark={self.mark!r}, release_year={self.release_year!r}, max_spped={self.max_speed!r})"


class CargoAuto(Auto):
    def __init__(self, mark: str, release_year: int, max_kg_weight: int):
        """
        Создание и подготовка к работе дочернео класса "Грузовой автомобиль"
        в дочернем классе появляется новый параметр
        :param max_kg_weight: Максимальный вес груза для данного автомобиля, кг
        #:param current_weight: вес груза в данный момент времени
        Примеры:
        >>> c = CargoAuto("Kamri", 2010, 1000)  # инициализация экземпляра класса
        """
        super().__init__(mark=mark, release_year=release_year)
        if not isinstance(max_kg_weight, int):
            raise TypeError("Максимальный вес должен быть типа float")
        if max_kg_weight < 0:
            raise ValueError("Максимальный вес не может быть меньше нуля")
        self.max_kg_weight = max_kg_weight

    def __str__(self):
        return f"{super().__str__()} и имеет максимальную вместимость {self.max_kg_weight}"

    def __repr__(self):
        return f"{self.__class__.__name__}(mark={self.mark!r}, release_year={self.release_year!r}, max_kg_weight={self.max_kg_weight!r})"

    def overweight(self, current_weihgt: int):
        """"
        Метод, который вычисляет, будет ли перегруз или нет
        :param current_weight: вес груза в данный момент времени
        :raise ValueError: Если current_weight будет больше max_kg_weight
        Примеры:
        >>> c = CargoAuto("Kamri", 2010, 2000)
        >>> c.overweight(500)
        """
        if not isinstance(current_weihgt, int):
            raise TypeError("Максимальный вес должен быть типа float")
        if current_weihgt < 0:
            raise ValueError("Максимальный вес не может быть меньше нуля")
        if current_weihgt > self.max_kg_weight:
            raise ValueError("Перегруз")

    def car_can_drive(self):
        """"
         Переопределяем Метод car_can_drive, который есть в родительском классе
         Допустим, по умолчанию любой легковой автомобиль может ездить
         Будет ехать грузовой автомобиль или нет зависит от веса груза - current_weihgt
         Метод будет работать, если current_weihgt < self.max_kg_weight
        """
        return f"Грузовой автомобиль марки {self.mark} с  грузом в {self.max_kg_weight} кг может ехать"


p = PassengerAuto("nissan", 2020, 120)
print(p)
print(p.car_can_drive()) #метод car_can_drive унаследован от родительского класса

c = CargoAuto("LADa", 2020, 1000)
print(c)
c.overweight(1000)
print(c.car_can_drive()) #метод car_can_drive переопределен


if __name__ == "__main__":
    doctest.testmod()
