# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания. При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину. При вычитании не допускайте отрицательных значений.

# Доработайте прошлую задачу. Добавьте сравнение прямоугольников по площади. Должны работать
# все шесть операций сравнения

class Rectangle:
    """
    Класс прямоугольник
    """

    def __init__(self, size1: int | float, size2: int | float | None = None):
        """
        :param size1: первый размер
        :param size2: второй размер. Если аргумент не передается, второй размер принимается равным первому
        """
        self._width = size1
        self._height = size2 or size1

    def get_perimeter(self) -> float:
        """
        Вычисляет и возвращает периметр
        :return: периметр
        """
        return 2 * (self._width + self._height)

    def get_area(self) -> float:
        """
        Вычисляет и возвращает площадь
        :return: площадь
        """
        return self._width * self._height

    def __add__(self, other):
        new_perimeter = self.get_perimeter() + other.get_perimeter()
        return Rectangle(self._width * new_perimeter / self.get_perimeter(),
                         self._height * new_perimeter / self.get_perimeter())

    def __sub__(self, other):
        new_perimeter = self.get_perimeter() - other.get_perimeter()
        if new_perimeter < 0:
            raise ArithmeticError
        return Rectangle(self._width * new_perimeter / self.get_perimeter(),
                         self._height * new_perimeter / self.get_perimeter())

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __str__(self):
        return f"Прямоугольник {self._width}x{self._height}. Периметр {self.get_perimeter()}, площадь {self.get_area()}"


if __name__ == '__main__':
    rect = Rectangle(12, 2)
    print(rect)

    rect2 = Rectangle(3, 8)
    print(rect2)

    square = Rectangle(2)
    print(square)

    sum_rect = rect + square
    print(sum_rect)

    sub_rect = rect - square
    print(sub_rect)

    print(f"{rect == rect2 = }")
    print(f"{rect > square = }")
    print(f"{rect < square = }")
    print(f"{rect != sub_rect = }")
    print(f"{rect >= sum_rect = }")
    print(f"{rect <= sum_rect = }")
