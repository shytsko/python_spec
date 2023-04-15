# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class Size:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int | float):
            raise TypeError(f'Значение {self.param_name} должно быть числового типа')
        if value <= 0:
            raise ValueError(f'Значение {self.param_name} должно быть положительным')


class Rectangle:
    """
    Класс прямоугольник
    """
    width = Size()
    height = Size()

    def __init__(self, size1: int | float, size2: int | float | None = None):
        """
        :param size1: первый размер
        :param size2: второй размер. Если аргумент не передается, второй размер принимается равным первому
        """
        self.width = size1
        self.height = size2 or size1

    def get_perimeter(self) -> float:
        """
        Вычисляет и возвращает периметр
        :return: периметр
        """
        return 2 * (self.width + self.height)

    def get_area(self) -> float:
        """
        Вычисляет и возвращает площадь
        :return: площадь
        """
        return self.width * self.height

    def __add__(self, other):
        new_perimeter = self.get_perimeter() + other.get_perimeter()
        return Rectangle(self.width * new_perimeter / self.get_perimeter(),
                         self.height * new_perimeter / self.get_perimeter())

    def __sub__(self, other):
        new_perimeter = self.get_perimeter() - other.get_perimeter()
        if new_perimeter < 0:
            raise ArithmeticError
        return Rectangle(self.width * new_perimeter / self.get_perimeter(),
                         self.height * new_perimeter / self.get_perimeter())

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __str__(self):
        return f"Прямоугольник {self.width}x{self.height}. Периметр {self.get_perimeter()}, площадь {self.get_area()}"


if __name__ == '__main__':
    rect = Rectangle(12, 2)
    print(rect)
    print(rect.__dict__)
    rect.width -= 4
    rect.height += 4
    print(rect)
    rect.width = 5.5
    print(rect)
