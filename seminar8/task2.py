# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

from pathlib import Path
from json import dump, load

LEVEL_MIN = 1
LEVEL_MAX = 7


def input_data(file: str | Path) -> None:
    if not isinstance(file, Path):
        file = Path(file)

    if not file.exists():
        data_dict = {str(level): [] for level in range(LEVEL_MIN, LEVEL_MAX + 1)}
    else:
        with file.open("r", encoding="utf-8") as f:
            data_dict = load(f)



    while True:

    with file.open("w", encoding="utf-8") as f:
        dump(data_dict, f, indent=2)


if __name__ == '__main__':
    input_data("task2.json")
