"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car():

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return (f'{self.name} - машина поехала')

    def stop(self):
        return (f"{self.name} - остановилась")

    def turn(self, direction):
        self.direction = direction
        return (f"{self.name} - повернула {direction}")

    def show_speed(self):
        return (f'текущая скорость: {self.name} составила {self.speed}')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'текущая скорость по городу: {self.name} составила {self.speed}')
        if self.speed > 60: return "Ваша скорость выше допусимой , по городу"
        else: return ('скорость в норме')

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def sport_car(self):
        if self.is_police: return (f"{self.name} спортивная машина")
        else: return (f'{self.name} не спортивная машина')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):

        print(f'текущая скорость для рабочего автомобиля: {self.name} составила {self.speed}')
        if self.speed > 40: return f'{self.name} ваша скорость для поездки на работу привышена'
        else: return f'{self.name} нормальная скорость'

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police: return (f'{self.name} полицейская машина')
        else: return (f'{self.name} не полицейская машина')


Toyota = TownCar(40, 'Серая', 'Тойота', False)
Toyota_cruiser = WorkCar(80, 'Черная', 'Лэнд Крузер', False)
Lada = SportCar(100, 'Синяя', 'Лада', False)
Ford = PoliceCar(130, 'Белая', 'Форд', True)


print(Toyota.show_speed())
print(Toyota_cruiser.show_speed())
print(Lada.show_speed())
print(Ford.show_speed())

print(Toyota.name)
print(Toyota_cruiser.name)
print(Lada.name)
print(Ford.name)

