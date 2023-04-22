class MyBaseException(Exception):
    pass


class IncorrectMatrixSize(MyBaseException):
    def __init__(self, *, rows_expected=None, columns_expected=None):
        self._rows_expected = rows_expected
        self._columns_expected = columns_expected

    def __str__(self):
        if self._rows_expected is not None and self._columns_expected is not None:
            return f"Размер матрицы справа должен быть {self._rows_expected} x {self._columns_expected}"
        elif self._rows_expected is not None:
            return f"Количество строк матрицы справа должно быть {self._rows_expected}"
        elif self._columns_expected is not None:
            return f"Количество столбцов матрицы справа должно быть {self._columns_expected}"
        else:
            return f"Не корректный размер матрицы справа"