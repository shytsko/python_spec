# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и
# директорий.
#
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов

import csv
import json
import pickle
from pathlib import Path

NAME_HEADER = "name"
PARENT_HEADER = "parent"
TYPE_HEADER = "type"
SIZE_HEADER = "size"


def generate_files_data(path: str | Path, json_file: str, csv_file: str, pickle_file: str) -> None:
    files_data = get_files_data_list(path)

    with open(json_file, "w", encoding="UTF-8") as f:
        json.dump(files_data, f, indent=2)

    with open(csv_file, "w", encoding="UTF-8", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=[NAME_HEADER, PARENT_HEADER, TYPE_HEADER, SIZE_HEADER], restval="",
                                    extrasaction="ignore", quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(files_data)

    with open(pickle_file, "wb") as f:
        pickle.dump(files_data, f)


def get_files_data_list(path: str | Path) -> list[dict]:
    if not isinstance(path, Path):
        path = Path(path)
    path = path.resolve()
    files_data = []
    _get_files_data_recursive(path, files_data)
    return files_data


def _get_files_data_recursive(path: Path, files_data: list[dict]) -> int:
    if path.is_file():
        file_size = path.stat().st_size
        files_data.append({
            NAME_HEADER: str(path),
            PARENT_HEADER: str(path.parent),
            TYPE_HEADER: "file",
            SIZE_HEADER: file_size
        })
        return file_size
    elif path.is_dir():
        dir_size = 0
        dir_data = {
            NAME_HEADER: str(path),
            PARENT_HEADER: str(path.parent),
            TYPE_HEADER: "dir",
            SIZE_HEADER: 0
        }
        files_data.append(dir_data)
        for file in path.iterdir():
            dir_size += _get_files_data_recursive(file, files_data)
        dir_data[SIZE_HEADER] = dir_size
        return dir_size


if __name__ == '__main__':
    generate_files_data("..", "files_data.json", "files_data.csv", "files_data.pickle")
