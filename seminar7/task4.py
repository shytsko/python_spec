# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.


import os
from random import randint, sample, randbytes
from string import ascii_letters


def files_generator(path: str, *, ext: str, min_name_len: int = 6, max_name_len: int = 30, min_file_size: int = 256,
                    max_file_size: int = 4096, count: int = 42) -> None:
    for _ in range(count):
        name_len = randint(min_name_len, max_name_len)
        size = randint(min_file_size, max_file_size)
        file_name = ''.join(sample(ascii_letters, name_len)) + f".{ext}"
        path = os.path.join(os.getcwd(), 'task4', file_name)
        with open(path, 'wb') as f:
            f.write(randbytes(size))


def file_generator_ex(path: str, *args, **kwargs) -> None:

    for i in range(0, len(args) & ~0b1, 2):
        if isinstance(args[i], str) and isinstance(args[i + 1], int):
            files_generator(ext=args[i], count=args[i + 1], max_name_len=10)

    for ext, count in kwargs.items():
        if isinstance(count, int):
            files_generator(ext=ext, count=count, max_name_len=10)


if __name__ == '__main__':
    file_generator_ex("txt", 3, "bin", 5, "data", 7, img=4, doc=1)
