# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1. Если передан один параметр, также считаем start=1.

from math import factorial


class FactorialGen:

    def __init__(self, *args):
        if len(args) == 1:
            self._num_iterator = iter(range(1, args[0]))
        else:
            self._num_iterator = iter(range(*args))

    def __iter__(self):
        return self

    def __next__(self):
        return factorial(next(self._num_iterator))


if __name__ == '__main__':
    print(*FactorialGen(20))
    print(*FactorialGen(5, 10))
    print(*FactorialGen(10, 20, 3))
