# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
import os
from random import randint, sample, randbytes
from string import ascii_letters


def files_generator(*, ext: str, min_name_len: int = 6, max_name_len: int = 30, min_file_size: int = 256,
                    max_file_size: int = 4096, count: int = 42) -> None:
    for _ in range(count):
        name_len = randint(min_name_len, max_name_len)
        size = randint(min_file_size, max_file_size)
        file_name = os.path.join(os.getcwd(), 'task4', ''.join(sample(ascii_letters, name_len)) + f".{ext}")
        with open(file_name, 'wb') as f:
            f.write(randbytes(size))


# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.
def file_generator_ex(extensions: dict[str, int]) -> None:
    for extension, files_count in extensions.items():
        files_generator(ext=extension, count=files_count)


if __name__ == '__main__':
    file_generator_ex({"txt": 3, "bin": 5, "data": 7})
