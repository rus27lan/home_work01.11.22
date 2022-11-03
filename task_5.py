"""
Задание 5.

Реализовать класс Stationery (канцелярская принадлежность).

Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”

Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).

В каждом из классов реализовать переопределение метода draw.

Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery():

    def __init__(self):
        self.title = print('Канцелярская пренадлежность')
    def draw(self):
        print('Запуск отрисовки\n')

class Pen(Stationery):

    def __init__(self):
        self.title = print('Ручка')

    def draw(self):
        print('Дочерний метод класса Pen\n')

class Pencil(Stationery):

    def __init__(self):
        self.title = print('Карандаш')

    def draw(self):
        print('Дочерний метод класса Pencil\n')

class Handle(Stationery):

    def __init__(self):
        self.title = print('Маркер')

    def draw(self):
        print('Дочерний метод класса Handle')

a = Stationery()
a.draw()

b = Pen()
b.draw()

c = Pencil()
c.draw()

d = Handle()
d.draw()