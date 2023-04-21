# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса

import pytest
from seminar12.task4 import Rectangle


@pytest.fixture
def test_rect1():
    return Rectangle(12, 2)


@pytest.fixture
def test_rect2():
    return Rectangle(10)


def test_get_perimeter(test_rect1):
    assert test_rect1.get_perimeter() == 28


def test_get_area(test_rect2):
    assert test_rect2.get_area() == 100


def test_square(test_rect2):
    assert str(
        test_rect2) == f"Прямоугольник 10x10. Периметр {test_rect2.get_perimeter()}, площадь {test_rect2.get_area()}"


if __name__ == '__main__':
    pytest.main()
