"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road():
    mass_of_asphalt_1m = 25
    thickness = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt(self):
        mass_asphalt = self._length * self._width * Road.mass_of_asphalt_1m * Road.thickness
        if mass_asphalt >= 1000: mass_asphalt = f"{mass_asphalt / 1000} т"
        else: mass_asphalt = f"{mass_asphalt} кг"
        return mass_asphalt

length_width = Road(20, 5000)

print(f"Потребуется: {length_width.asphalt()}")