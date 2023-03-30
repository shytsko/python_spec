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

# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


import os
from random import randint, sample, randbytes
from string import ascii_letters
from pathlib import Path


def random_files_creator(dir_path: Path, *, ext: str, min_name_len: int = 6, max_name_len: int = 30, min_file_size: int = 256,
                         max_file_size: int = 4096, count: int = 42) -> None:
    while count > 0:
        name_len = randint(min_name_len, max_name_len)
        size = randint(min_file_size, max_file_size)
        file_name = ''.join(sample(ascii_letters, name_len)) + f".{ext}"
        file_path = dir_path / file_name
        if not file_path.exists():
            with file_path.open('wb') as f:
                f.write(randbytes(size))
            count -= 1


def file_generator_ex(dir_path: str | Path, *args, **kwargs) -> None:
    if not isinstance(dir_path, Path):
        dir_path = Path(dir_path)

    if not dir_path.exists():
        dir_path.mkdir(parents=True)
    elif not dir_path.is_dir():
        return

    for i in range(0, len(args) & ~0b1, 2):
        if isinstance(args[i], str) and isinstance(args[i + 1], int):
            random_files_creator(dir_path=dir_path, ext=args[i], count=args[i + 1], max_name_len=10)

    for ext, count in kwargs.items():
        if isinstance(count, int):
            random_files_creator(dir_path=dir_path, ext=ext, count=count, max_name_len=10)


if __name__ == '__main__':
    file_generator_ex(r"files", "txt", 3, "bin", 5, "data", 7, img=4, doc=1)
