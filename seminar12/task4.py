# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.

class Rectangle:
    """
    Класс прямоугольник
    """
    __slots__ = ["_width", "_height"]
    def __init__(self, size1: int | float, size2: int | float | None = None):
        """
        :param size1: первый размер
        :param size2: второй размер. Если аргумент не передается, второй размер принимается равным первому
        """
        self.width = size1
        self.height = size2 or size1


    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width cannot be equal to or less than 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height cannot be equal to or less than 0")
        self._height = value

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
    # print(rect.__dict__)
    rect.width -= 4
    rect.height += 4
    print(rect)
    # rect.width += 6
    # rect.height -= 8
    # print(rect)

    # rect = Rectangle(0, 2)