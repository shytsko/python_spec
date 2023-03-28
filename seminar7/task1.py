# ✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform

MIN_VALUE = -1000
MAX_VALUE = 1000


def fun(file_name, count):
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(count):
            print(f"{randint(MIN_VALUE, MAX_VALUE)}|{uniform(MIN_VALUE, MAX_VALUE)}", file=f)


if __name__ == '__main__':
    fun("file1.txt", 3)
