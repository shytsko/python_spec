# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.
from typing import Any


def my_get(dict_: dict[Any, Any], key: Any, default: Any = None) -> Any:
    try:
        return dict_[key]
    except KeyError as e:
        return default


if __name__ == '__main__':
    test_dict = {1: "dfgs", 2: 5.564, 3: [1, 2, 3], "abc": 42}
    print(my_get(test_dict, 1, 100))
    print(my_get(test_dict, 2, 100))
    print(my_get(test_dict, 3, 100))
    print(my_get(test_dict, 4, 100))
    print(my_get(test_dict, 4))
