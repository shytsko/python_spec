# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.
import json
from pprint import pprint


class User:
    def __init__(self, id_, name, level = 0):
        self._id = id_
        self._name = name
        self._level = level

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    def __repr__(self):
        return f"User({self._id}, {self._name}, {self._level})"

    def __eq__(self, other):
        return self._id == other._id and self._name == other._name

    def __hash__(self):
        return hash((self._id, self._name))


def load_users(file_name) -> set[User]:
    with open(file_name, "r", encoding="UTF-8") as f:
        json_data = json.load(f)

    return {User(int(id_), name, int(level)) for level, users in json_data.items() for id_, name in users.items()}


if __name__ == '__main__':
    pprint(load_users("../seminar8/task2.json"))
