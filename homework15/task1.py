# Использована функция для создания файлов из семинара 7

from file_utils import random_files_creator_ex
import logging
import argparse
from pathlib import Path

if __name__ == '__main__':
    logging.basicConfig(filename="task1.log", filemode="w", encoding="utf-8", level=logging.NOTSET)
    logger = logging.getLogger(__name__)
    parser = argparse.ArgumentParser(description='Создает файлы с заданным расширением и количеством')
    parser.add_argument('path', help='Путь к каталогу для сохранения файлов', type=Path)
    parser.add_argument('-e', metavar=('<ext>', '<count>'), help='расширение и количество файлов', nargs=2,
                        action='append')
    args = parser.parse_args()
    logger.info(f"Переданы параметры: {args}")
    try:
        extensions = {ext: int(count) for ext, count in args.e}
    except ValueError:
        logger.error("Ошибка в параметрах")
    else:
        logger.info(f"Будут созданы файлы {extensions} в каталоге {args.path.absolute()}")
        random_files_creator_ex(args.path, **extensions)
