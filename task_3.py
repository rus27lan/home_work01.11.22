"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""

class Worker():

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 10000, "bonus": 15000}

first_worker = Worker('Anna', 'Maximova', 'director')

class Position(Worker):

    def get_full_name(self):
        full_name = f"{first_worker.name} {first_worker.surname}"
        return full_name

    def get_total_income(self):
        return f"доход с учетом премии: {self._income['wage'] + self._income['bonus']}"

pos = Position('Anna', 'Maximova', 'director')

print(pos.get_full_name())
print(pos.get_total_income())