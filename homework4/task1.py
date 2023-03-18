# Напишите функцию для транспонирования матрицы


test_matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [20, 21, 22, 23, 24]]


def transpose_matrix(matrix: list[list[int]]) -> bool:
    matrix_size = len(matrix)

    if any(map(lambda x: len(x) != matrix_size, matrix)):
        return False

    for i in range(1, matrix_size):
        for j in range(0, i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def print_matrix(matrix: list[list[int]]):
    for row in matrix:
        for item in row:
            print(f"{item:4}", end="")
        print()


print("Исходная матрица")
print_matrix(test_matrix)
transpose_matrix(test_matrix)
print("\nТранспонированная матрица")
print_matrix(test_matrix)