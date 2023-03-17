# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком. Её описание есть в википедии.

array = [5, 3, 9, 7, 0, -8, 4, 7, 5]


def sort_(items: list) -> None:
    for i in range(len(items) - 1):
        for j in range(i + 1, len(items)):
            if items[i] > items[j]:
                items[i], items[j] = items[j], items[i]

print(array)
sort_(array)
print(array)
