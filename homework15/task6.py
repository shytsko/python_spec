# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

from collections import namedtuple
import argparse
import logging
from pathlib import Path


def get_data(path):
    root = Path(path)
    FileData = namedtuple("FileData", ["name", "extension", "is_dir", "parent"])
    logger = logging.getLogger()
    if not root.exists() or not root.is_dir():
        return
    for file in root.iterdir():
        data = FileData(name=file.stem,
                        extension=file.suffix if not file.is_dir() else None,
                        is_dir=file.is_dir(),
                        parent=str(file.parent))
        logger.info(f"{data}")
        if file.is_dir():
            get_data(file)


if __name__ == '__main__':
    logging.basicConfig(filename="task6.log", filemode="w", encoding="utf-8", level=logging.NOTSET)
    parser = argparse.ArgumentParser(description='Сбор данных о файлах в каталоге')
    parser.add_argument('path', metavar='path', help='Путь к каталогу')
    args = parser.parse_args()
    get_data(args.path)
