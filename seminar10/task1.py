# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
from math import pi


class Circle:
    def __init__(self, radius: int | float):
        self.radius = radius

    def get_length(self) -> float:
        return 2 * pi * self.radius

    def get_area(self) -> float:
        return pi * self.radius ** 2


if __name__ == '__main__':
    circle = Circle(5)
    print(circle.get_length())
    print(circle.get_area())
