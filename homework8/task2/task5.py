# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import json
import pickle
from pathlib import Path

__all__ = ["find_and_convert_json_pickle"]


def find_json(path: Path) -> list[Path]:
    return list(path.glob("*.json"))


def convert_json_to_pickle(file_json: Path) -> Path:
    with file_json.open("r", encoding="utf-8") as f:
        data = json.load(f)
    file_pickle = file_json.with_suffix(".pickle")
    with file_pickle.open("wb") as f:
        pickle.dump(data, f)


def find_and_convert_json_pickle(path: str | Path) -> None:
    if not isinstance(path, Path):
        path = Path(path)

    if not path.is_dir():
        print("Path is not directiory")
        return

    json_files = find_json(path)
    for file in json_files:
        convert_json_to_pickle(file)


if __name__ == '__main__':
    find_and_convert_json_pickle(".")
