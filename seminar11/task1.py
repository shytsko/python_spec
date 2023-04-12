# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)
from os import getlogin
from time import time, strftime, localtime, gmtime


class StrExt(str):
    """
    Класс расширяет стандартный тип str. Дополнительно хранит имя пользователя и время создания.
    """

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance._author = getlogin()
        instance._create_time = time()
        return instance

    def __str__(self):
        return f"{self._author}: {strftime('%H:%M:%S %z', gmtime(self._create_time))}: {super().__str__()}"

    def __repr__(self):
        return f"StrExt({super().__repr__()})"


if __name__ == '__main__':
    my_str = StrExt("Создайте класс Моя Строка")
    print(my_str)
    print(StrExt(my_str.upper()))

    print(my_str.split())
    print(my_str[9:14])

    print(f"{my_str = }")


