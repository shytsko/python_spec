# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.

from math import factorial
import json


class Factorial:
    def __init__(self, cache_size, json_file_name):
        self._cache_size = cache_size
        self._json_file_name = json_file_name
        self._cache = {}
        self._json_file = None

    def __call__(self, value, *args, **kwargs):
        if value not in self._cache:
            if len(self._cache) == self._cache_size:
                self._cache.pop(next(iter(self._cache)))
            self._cache[value] = factorial(value)
        return self._cache[value]

    def view_cache(self):
        return str(self._cache)

    def __enter__(self):
        self._json_file = open(self._json_file_name, "w", encoding="UTF-8")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._json_file:
            json.dump(self._cache, self._json_file)
            self._json_file.close()
            self._json_file = None


if __name__ == '__main__':
    with Factorial(5, "cache.json") as fact:
        print(fact(10))
        print(fact(4))
        print(fact(8))
        print(fact(15))
        print(fact(5))
        print(fact(20))
        print(fact(10))
        print(fact(5))
        print(fact.view_cache())
