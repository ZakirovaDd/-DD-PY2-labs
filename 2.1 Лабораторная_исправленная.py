import doctest


class Train:
    def __init__(self, speed: float, num_of_passengers: int, max_number_of_passagers: int):
        """
        Создание и подготовка к работе объекта "Поезд"
        :param speed: Скорость, с которой едет поезд
        :param num_of_passengers: Число пассажиров в поезде в данный момент времени
        :param max_number_of_passagers: Максимальное число пассажиров, которые могут ехать в данном поезде
        Примеры:
        >>> train = Train(120, 300,400)  # инициализация экземпляра класса
        """
        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость поезда должна быть типа int или float")
        if speed <= 0:
            raise ValueError("Скорость должен быть положительным числом")
        if speed >= 200:
            raise ValueError("Скорость пассажирского поезда в ржд не может быть больше 200 км в час")
        self.speed = speed

        if not isinstance(num_of_passengers, int):
            raise TypeError("Количество пассажиров должно быть int")
        if num_of_passengers < 0:
            raise ValueError("Количество пассажиров должно быть положительным числом")
        if num_of_passengers > max_number_of_passagers:
            raise ValueError("Вместимость поезда - 450 пассажиров. Больше пассажиров ехать в одном поеде не может")
        self.num_of_passengers = num_of_passengers

        if not isinstance(max_number_of_passagers, int):
            raise TypeError("Количество пассажиров должно быть int")
        if max_number_of_passagers < 0:
            raise ValueError("Максимальное количество пассажиров должно быть положительным числом")
        if max_number_of_passagers > 450:
            raise ValueError("Максимальная вместимость поезда - 450 пассажиров. Больше пассажиров ехать в одном поеде не может")
        self.max_number_of_passagers = max_number_of_passagers

    def empty_train(self) -> bool:
        """
        Функция которая проверяет есть в поезде пассажиры или нет
        :return: Является ли поезд пустым
        Примеры:
        >>> train = Train(120, 0,400)
        >>> train.empty_train()
        """
        ...

    def new_passagers(self, passagers: int) -> int:
        """
        Пусть на остановке быдут заходить новые пассажиры в поезд .
        :param passagers: Новые пассажиры, вошедшие в поезд
        :raise ValueError: Если количество пассажиров больше 450
        Примеры:
        >>> train = Train(120, 100,400)
        >>> train.new_passagers(200)
        """
        if not isinstance(passagers, int):
            raise TypeError("Пассажиры должны быть типа int или float")
        if passagers < 0:
            raise ValueError("Пассажиры должны положительным числом")
        if self.num_of_passengers + passagers > self.max_number_of_passagers:
            raise ValueError("Пассажиров не может быть больше 450")

        self.num_of_passengers += passagers



class Teapot:
    def __init__(self, capacity_volume: float, occupied_volume: float, power: int):
        """
        Создание и подготовка к работе объекта "Чайник"
        :param capacity_volume: Объем чайника (в л)
        :param occupied_volume: Объем занимаемой жидкости в чайнике (в л)
        :param power: мощность чайника (в Вт)
        Примеры:
        >>> teapot = Teapot(2, 0.35, 2000)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем чайника должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем чайника должен быть положительным числом")
        if capacity_volume > 3:
            raise ValueError("Объем чайника не должен быть больше 3 литров")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости в чайнике должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        if occupied_volume > capacity_volume:
            raise ValueError("Количество жидкости не может быть больше объема чайника")
        self.occupied_volume = occupied_volume

        if not isinstance(power, int):
            raise TypeError("Мощность чайника должна быть типа int")
        if power > 3000:
            raise ValueError("Слишком большая мощность для чайника")
        if power < 0:
            raise ValueError("Мощность чайника должна быть больше 0")
        self.power = power


    def empty_teapot(self) -> bool:
        """
        Функция которая проверяет является ли чайник пустым
        :return: Является ли чайник пустым
        Примеры:
        >>> teapot = Teapot(1.5, 0,1500)
        >>> teapot.empty_teapot()
        """
        ...

    def boiling_time(self, temperatur_first: int) -> float:
        """
        ПУсть наша функция рассчитывает время закипания чайника, зная начальную теммпературу воды в чайнике
        Тогда Q=cm(t2-t1)=PT, тогда T=cm(t2-t1)/P, где Р - мощность, t2 =100 градусов, c = 4200 (const Для воды)
        и m = V
        :param temperatur_first: начальная температрура
        :raise ValueError: Если начальная температура будет больше конечно или будет меньше 0
        :return: Время закипания чайника (с)
        Примеры:
        >>> teapot = Teapot(2, 0.35, 2000)
        >>> teapot.boiling_time(20)
        """
        temperatur_second = 100
        # Вода закипает при 100 градусах
        conductivity_of_water = 4200
        # удельная теплопроводность воды
        if not isinstance(temperatur_first, int):
            raise TypeError("Температура воды должна быть типа int")
        if temperatur_first <= 0:
            raise ValueError("Температура должна быть положительным числом ")
        if temperatur_first > temperatur_second:
            raise ValueError("Начальная температура не может быть больше конечной")
        self.temperatur_first = temperatur_first

        time = (self.occupied_volume * conductivity_of_water * (temperatur_second - temperatur_first))/self.power
        # return time

    def service_life(self, inclusion_time: int):
        """
        Пусть у чайника будет конкретное конечное количество включений - то есть время работы нашего чайника.
        Предположим срок службы чайника количества включений.
        :param inclusion_time: Сколько раз за день чайник включали
        :raise ValueError: Если чайник сломается
        :return: сколько может прослужить чайник (лет)
        Примеры:
        >>> teapot = Teapot(2, 0.5, 2000)
        >>> teapot.service_life(10)
        """
        if not isinstance(inclusion_time, int):
            raise TypeError("Количество включений чайника должно быть типа int")
        if inclusion_time < 0:
            raise ValueError("Количество включений в день не должно быть отрицательным числом")
        self.inclusion_time = inclusion_time
        ...



class Person:
    def __init__(self, name: str, age: int, hp: int):
        """
        Создание и подготовка к работе объекта "Персонаж"
        :param name: Имя персонажа
        :param age: Возраст персонажа
        :param hp:  здоровье персонажа, текущее
        Примеры:
        >>> person = Person("Кирилл", 20, 100)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя персонажа должно быть типа str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст персонажа должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст персонажа может быть только положительны числом")
        self.age = age

        self.damage = 10
        #урон, который может получить персонаж
        self.max_hp = 100
        # Максимальное здоровье персонажа

        if not isinstance(hp, int):
            raise TypeError("Здоровье персонажа должно быть типа int")
        if hp <= 0:
            raise ValueError("Персонаж умер")
        if hp > self.max_hp:
            raise ValueError("Максимальное здоровье персонажа 100")
        self.hp = hp



    def fall(self, height: int):
        """
        ПУсть персонаж падает с n-высоты и получает урон. При этом получаемый урон будет произведением damage*height
        :param height: высота
        :raise ValueError: Если полученный урон будет больше максимального здоровья, вызываем ошибку "Герой умер"
        :return: Ноове хп персонажа
        Примеры:
        >>> person = Person("Кирилл", 20, 100)
        >>> person.fall(3)
        """
        if not isinstance(height, int):
            raise TypeError("Высота должна быть типа int")
        if height < 0:
            raise ValueError("Высота должна быть не отрицательным числом")
        if self.damage * height > self.max_hp:
            raise ValueError("Персонаж умер")

        self.hp = self.max_hp - (self.damage*height)

    def increase_hp(self, heal: int):
        """
        Персонаж может лечиться и тем самым повышать здоровье.
        :param heal: Полученное лечение
        :raise ValueError: Если полученное лечение больше максимального хп
        :return: Ноове хп персонажа
        Примеры:
        >>> person = Person("Кирилл", 20, 10)
        >>> person.increase_hp(15)
        """
        if not isinstance(heal, int):
            raise TypeError("Полученное лечение должно быть типа int")
        if heal < 0:
            raise ValueError("Полученное лечение быть не отрицательным числом")
        if self.hp + heal > self.max_hp:
            raise ValueError("Полученное лечение не может быть больше максимального хп")

        self.hp += heal


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
print(dir(Train))