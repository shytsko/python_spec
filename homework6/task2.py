# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

from my_pack import check_queens_solution, view_queens_solution

true_solution = ((3, 0), (7, 1), (0, 2), (2, 3), (5, 4), (1, 5), (6, 6), (4, 7))
false_solution = ((0, 0), (7, 1), (1, 2), (6, 3), (2, 4), (5, 5), (3, 6), (4, 7))

print(check_queens_solution(true_solution))
view_queens_solution(true_solution)
print()
print(check_queens_solution(false_solution))
view_queens_solution(false_solution)