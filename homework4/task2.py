# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ —
# значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление

def get_argument_dict(**kwargs) -> dict[any, str]:
    names, values = zip(*kwargs.items())
    values_hashable = map(convert_to_hashable, values)
    return dict(zip(values_hashable, names))


def convert_to_hashable(object):
    return object if isinstance(object, (str, int, bool, float, tuple, frozenset)) else str(object)


print(get_argument_dict(arg1=8, arg2="dfgsghsgdg", arg3=[4, 7, 3, 7, 9, ], arg4={3, 7, 9, 2},
                        arg5=frozenset((4, 7, 9, 2))))
