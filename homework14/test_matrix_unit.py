from matrix import Matrix
import unittest
from exceptions import IncorrectMatrixSize


class TestMatrix(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.matrix1 = Matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 141, 142, 143], [15, 16, 17, 18]])
        cls.matrix2 = Matrix([[1, 2, 3, 4], [6, 7, 8, 9], [12, 13, 14, 141], [15, 16, 17, 18]])
        cls.matrix3 = Matrix([[1, 2, 1, 2], [2, 1, 1, 2], [2, 2, 2, 2], [1, 1, 1, 1]])
        cls.matrix5 = Matrix([[1, -1], [2, 0], [3, 0]])
        cls.matrix6 = Matrix([[1, 1, -1, 4], [2, 0, 1, 6]])

    def test_eq(self):
        self.assertEqual(self.matrix1, self.matrix2)

    def test_not_eq(self):
        self.assertNotEqual(self.matrix1, self.matrix3)

    def test_str(self):
        self.assertEqual(str(self.matrix1),
                         '    1     2     3     4\n'
                         '    6     7     8     9\n'
                         '   12    13    14   141\n'
                         '   15    16    17    18')
        self.assertEqual(str(self.matrix6), '    1     1    -1     4\n    2     0     1     6')

    def test_add(self):
        sum_matrix = self.matrix1 + self.matrix3
        self.assertEqual(sum_matrix, Matrix([[2, 4, 4, 6], [8, 8, 9, 11], [14, 15, 16, 143], [16, 17, 18, 19]]))

    def test_add_incorrect(self):
        with self.assertRaisesRegex(IncorrectMatrixSize, 'Размер матрицы справа должен быть 4 x 4'):
            self.matrix1 + self.matrix5

    def test_mul(self):
        mul_matrix = self.matrix5 * self.matrix6
        self.assertEqual(mul_matrix, Matrix([[-1, 1, -2, -2], [2, 2, -2, 8], [3, 3, -3, 12]]))

    def test_mul_incorrect(self):
        with self.assertRaisesRegex(IncorrectMatrixSize, 'Количество столбцов матрицы справа должно быть 4'):
            self.matrix1 * self.matrix5


if __name__ == '__main__':
    unittest.main(verbosity=2)
