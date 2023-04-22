# Задача из ДЗ 11
# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц
from Exceptions import IncorrectMatrixSize


class Matrix:
    """
    >>> matrix1 = Matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 141, 142, 143], [15, 16, 17, 18]])
    >>> print(matrix1)
        1     2     3     4
        6     7     8     9
       12    13    14   141
       15    16    17    18
    >>> matrix2 = Matrix([[1, 2, 3, 4], [6, 7, 8, 9], [12, 13, 14, 141], [15, 16, 17, 18]])
    >>> matrix3 = Matrix([[1, 2, 1, 2], [2, 1, 1, 2], [2, 2, 2, 2], [1, 1, 1, 1]])
    >>> matrix2 == matrix1
    True
    >>> matrix2 == matrix3
    False
    >>> sum_matrix = matrix1 + matrix3
    >>> print(sum_matrix)
        2     4     4     6
        8     8     9    11
       14    15    16   143
       16    17    18    19
    >>> matrix5 = Matrix([[1, -1], [2, 0], [3, 0]])
    >>> matrix6 = Matrix([[1, 1, -1, 4], [2, 0, 1, 6]])
    >>> mul_matrix = matrix5 * matrix6
    >>> print(mul_matrix)
       -1     1    -2    -2
        2     2    -2     8
        3     3    -3    12
    >>> sum_matrix = matrix1 + matrix5
    Traceback (most recent call last):
    ...
    Exceptions.IncorrectMatrixSize: Размер матрицы справа должен быть 4 x 4
    >>> mul_matrix = matrix1 * matrix5
    Traceback (most recent call last):
    ...
    Exceptions.IncorrectMatrixSize: Количество столбцов матрицы справа должно быть 4
    """

    def __init__(self, init_data: list[list[int | float]]):
        self._rows_count = len(init_data)
        self._columns_count = min(map(len, init_data))
        self._data = [row[0:self._columns_count] for row in init_data]

    def __str__(self):
        return "\n".join((" ".join(map(lambda x: f"{x:5}", row)) for row in self._data))

    def __eq__(self, other):
        return self._data == other._data

    def __add__(self, other):
        if self._rows_count != other._rows_count or self._columns_count != other._columns_count:
            raise IncorrectMatrixSize(rows_expected=self._rows_count, columns_expected=self._columns_count)
        return Matrix([[sum(x) for x in zip(self._data[i], other._data[i])] for i in range(self._rows_count)])

    def __mul__(self, other):
        if self._columns_count != other._rows_count:
            raise IncorrectMatrixSize(columns_expected=self._columns_count)

        return Matrix([[sum(map(lambda x: x[0] * x[1], zip(r, c))) for c in zip(*other._data)] for r in self._data])


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

