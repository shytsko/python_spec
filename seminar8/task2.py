# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

from pathlib import Path
from json import dump, load
from pprint import pprint

LEVEL_MIN = 1
LEVEL_MAX = 7


def input_data(file: str | Path) -> None:
    if not isinstance(file, Path):
        file = Path(file)

    if not file.exists():
        data_dict = {str(level): {} for level in range(LEVEL_MIN, LEVEL_MAX + 1)}
    else:
        with file.open("r", encoding="utf-8") as f:
            data_dict = load(f)

    while True:
        pprint(data_dict)
        name = input("Введите имя: ")
        if name == "":
            break
        id_ = input("Введите идентификатор: ")
        if id_ in {i for users in data_dict.values() for i in users.keys()}:
            print("Такой идентификатор уже есть")
            continue
        level = input("Введите уровень доступа: ")
        if level not in data_dict.keys():
            print("Уровень доступа должен быть от 1 до 7")
            continue
        data_dict[level][id_] = name

    with file.open("w", encoding="utf-8") as f:
        dump(data_dict, f, indent=2)


if __name__ == '__main__':
    input_data("task2.json")
