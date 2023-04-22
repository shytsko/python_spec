from matrix import Matrix
import pytest
from exceptions import IncorrectMatrixSize


@pytest.fixture
def matrix1():
    return Matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 141, 142, 143], [15, 16, 17, 18]])


@pytest.fixture
def matrix2():
    return Matrix([[1, 2, 3, 4], [6, 7, 8, 9], [12, 13, 14, 141], [15, 16, 17, 18]])


@pytest.fixture
def matrix3():
    return Matrix([[1, 2, 1, 2], [2, 1, 1, 2], [2, 2, 2, 2], [1, 1, 1, 1]])


@pytest.fixture
def matrix5():
    return Matrix([[1, -1], [2, 0], [3, 0]])


@pytest.fixture
def matrix6():
    return Matrix([[1, 1, -1, 4], [2, 0, 1, 6]])


def test_eq(matrix1, matrix2):
    assert matrix1 == matrix2, "Матрицы должны быть равны"


def test_not_eq(matrix1, matrix3):
    assert matrix1 != matrix3, "Матрицы должны быть не равны"


def test_str(matrix1, matrix6):
    assert str(matrix1) == \
           "    1     2     3     4\n    6     7     8     9\n   12    13    14   141\n   15    16    17    18", \
        "Не верное преобразование в строку"

    assert str(matrix6) == "    1     1    -1     4\n    2     0     1     6", "Не верное преобразование в строку"


def test_add(matrix1, matrix3):
    sum_matrix = matrix1 + matrix3
    assert sum_matrix == Matrix([[2, 4, 4, 6], [8, 8, 9, 11], [14, 15, 16, 143], [16, 17, 18, 19]]), \
        "Не верный результат сложения"


def test_add_incorrect(matrix1, matrix5):
    with pytest.raises(IncorrectMatrixSize, match="Размер матрицы справа должен быть 4 x 4"):
        matrix1 + matrix5


def test_mul(matrix5, matrix6):
    mul_matrix = matrix5 * matrix6
    assert mul_matrix == Matrix([[-1, 1, -2, -2], [2, 2, -2, 8], [3, 3, -3, 12]]), "Не верный результат умножения"


def test_mul_incorrect(matrix1, matrix5):
    with pytest.raises(IncorrectMatrixSize, match="Количество столбцов матрицы справа должно быть 4"):
        matrix1 * matrix5


if __name__ == '__main__':
    pytest.main()
