# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц


class Matrix(list):
    def __init__(self, init_data: list[list[int | float]]):
        self._rows_count = len(init_data)
        self._columns_count = min(map(len, init_data))
        self.extend((row[0:self._columns_count] for row in init_data))



if __name__ == '__main__':
    mtx = Matrix([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10, 11],
                  [12, 13, 14, 141, 142, 143],
                  [15, 16, 17, 18]])

    print(mtx)
