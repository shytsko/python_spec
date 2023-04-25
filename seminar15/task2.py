# На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её работы
# в файл. Напишите аналогичный декоратор, но внутри используйте модуль logging.

# Доработаем задачу 2. Сохраняйте в лог файл раздельно:
# уровень логирования,
# дату события,
# имя функции (не декоратора),
# аргументы вызова,
# результат.


import logging
from functools import wraps

LOG_FORMAT = "{levelname:<8}:{asctime}:{name}:{lineno:03d}:{msg}"


def log_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        logger = logging.getLogger(__name__)
        logger.info(f"{func.__name__}:{args=}:{kwargs=}:{res=}")
        return res

    return wrapper


@log_result
def fun1(n1, /, n2, n3):
    return 555


@log_result
def fun2(*args, **kwargs):
    return 777


if __name__ == '__main__':
    logging.basicConfig(filename="task2.log", filemode="a", encoding="utf-8", level=logging.NOTSET,
                        format=LOG_FORMAT, style="{")
    fun1(1, 2, 3)
    fun1(1, n3=2, n2=3)
    fun2("dbgdfhf", (0, 0, 0, 0), 2453, arg1=1, arg2=2)
    print(fun2.__name__)
