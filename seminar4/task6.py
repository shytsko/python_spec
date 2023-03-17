# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

source_array = [5, 8, 0, 6, 7, -9, 10, -6, 8, 4, 1]


def sum_range(array: list[int | float], index1: int, index2: int) -> int | float:
    start_index = max(min(index1, index2), 0)
    end_index = min(max(index1, index2), len(array) - 1)
    return sum(array[start_index:end_index + 1])


print(sum_range(source_array, 3, 8))
print(sum_range(source_array, 8, 3))
print(sum_range(source_array, -3, 3))
print(sum_range(source_array, 15, 6))
