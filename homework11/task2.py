# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц


class Matrix:
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
            raise ArithmeticError("Мatrix sizes are not equal.")
        return Matrix([[sum(x) for x in zip(self._data[i], other._data[i])] for i in range(self._rows_count)])

    def __mul__(self, other):
        if self._columns_count != other._rows_count:
            raise ArithmeticError(
                "The number of columns of the first matrix must be equal to the number of rows of the second matrix.")

        return Matrix([[sum(map(lambda x: x[0] * x[1], zip(r, c))) for c in zip(*other._data)] for r in self._data])


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2, 3, 4, 5],
                      [6, 7, 8, 9, 10, 11],
                      [12, 13, 14, 141, 142, 143],
                      [15, 16, 17, 18]])

    matrix2 = Matrix([[1, 2, 3, 4],
                      [6, 7, 8, 9],
                      [12, 13, 14, 141],
                      [15, 16, 17, 18]])

    matrix3 = Matrix([[1, 2, 1, 2],
                      [2, 1, 1, 2],
                      [2, 2, 2, 2],
                      [1, 1, 1, 1]])

    print(f"matrix1=\n{matrix1}\n")
    print(f"matrix2=\n{matrix2}\n")
    print(f"matrix3=\n{matrix3}\n")
    print(f"{matrix2 == matrix1 = }\n")
    print(f"{matrix2 == matrix3 = }\n")

    sum_matrix = matrix1 + matrix3
    print(f"sum_matrix = matrix1 + matrix3\n{sum_matrix}\n")

    matrix5 = Matrix([[1, -1],
                      [2, 0],
                      [3, 0]])

    matrix6 = Matrix([[1, 1, -1, 4],
                      [2, 0, 1, 6]])

    print(f"matrix5=\n{matrix5}\n")
    print(f"matrix6=\n{matrix6}\n")
    mul_matrix = matrix5 * matrix6
    print(f"mul_matrix = matrix5 + matrix6\n{mul_matrix}\n")

