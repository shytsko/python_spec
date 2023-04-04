# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции
import json
from pathlib import Path


def save_call_result(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res_dict = {"args": [*args], **kwargs, "res": res}
        file = Path(f"{func.__name__}.json")
        if file.exists():
            with file.open("r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = []
        data.append(res_dict)
        with open(f"{func.__name__}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return res

    return wrapper


@save_call_result
def fun1(n1, /, n2, n3):
    return 555


@save_call_result
def fun2(*args, **kwargs):
    return 777


fun1(1, 2, 3)
fun1(1, n3=2, n2=3)
fun2("dbgdfhf", (0, 0, 0, 0), 2453, arg1=1, arg2=2)
