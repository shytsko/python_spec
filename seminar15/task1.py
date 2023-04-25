# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging


def divider(arg1, arg2, log):
    try:
        return arg1 / arg2
    except ZeroDivisionError as e:
        log.error(e)


if __name__ == '__main__':
    logging.basicConfig(filename="log.log", filemode="a", encoding="utf-8", level=logging.NOTSET)
    logger = logging.getLogger(__name__)
    print(divider(5, 2, logger))
    print(divider(5, 0, logger))


