# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для
# случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и
# выведите 4 успешных расстановки.

from my_pack import check_queens_solution, view_queens_solution, get_random_queens_set

count_true_solution = 0

while count_true_solution < 4:
    solution = get_random_queens_set()
    if check_queens_solution(solution):
        count_true_solution += 1
        print(f"Правильное решение {count_true_solution}:")
        view_queens_solution(solution)
        print()
