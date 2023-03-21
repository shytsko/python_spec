# Напишите функцию для транспонирования матрицы


test_matrix = [[1, 2, 3],
               [6, 7, 8],
               [11, 12, 13],
               [16, 17, 18],
               [20, 21, 22]]


def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    new_rows_from_columns = zip(*matrix)
    return list(new_rows_from_columns)


def print_matrix(matrix: list[list[int]]):
    for row in matrix:
        for item in row:
            print(f"{item:4}", end="")
        print()


print("Исходная матрица")
print_matrix(test_matrix)
matrix_transposed = transpose_matrix(test_matrix)
print("\nТранспонированная матрица")
print_matrix(matrix_transposed)
