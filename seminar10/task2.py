# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат


class Rectangle:
    def __init__(self, size1: int | float, size2: int | float | None = None):
        self._width = size1
        self._height = size2 or size1

    def get_perimeter(self) -> float:
        return 2 * (self._width + self._height)

    def get_area(self) -> float:
        return self._width * self._height


if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(rect.get_perimeter())
    print(rect.get_area())

    square = Rectangle(2)
    print(square.get_perimeter())
    print(square.get_area())
