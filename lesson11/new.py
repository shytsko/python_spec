import sys
import time


class User:
    def __init__(self, name):
        self._name = name

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        # return instance
        return 42


class StrEx(str):
    def __new__(cls, value):
        instance = super().__new__(cls, value + "!!!")
        return instance

    def __del__(self):
        print(f"Deleted object {id(self)}")


class Singlton:
    """
    Pattern singleton example
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Dunder method __new__"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == '__main__':
    user = User("user")
    print(user, type(user))

    my_str = StrEx("qwerty")
    print(my_str, type(my_str))
    print(my_str.find("!!!"))
    my_str2 = my_str
    print(sys.getrefcount(my_str2))
    del my_str
    print(sys.getrefcount(my_str2))
    del my_str2

    first = Singlton()
    second = Singlton()
    print(f"{id(first) = } {id(second) = }")
    help(Singlton)
    help(Singlton.__new__)
    help(first.__new__)
