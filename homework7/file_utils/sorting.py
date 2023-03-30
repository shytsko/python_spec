from pathlib import Path

__all__ = ["files_sorting"]


def files_sorting(dir_path: Path | str, groups: dict[str, list[str]]) -> None:
    """
    Сортирует файлы по каталогам. Для каждой группы файлов создает отдельный вложенный каталог
    :param dir_path: Путь к каталогу с файлами
    :param groups: словарь, в которм ключ это название группы файлов, значение - список расширений файлов, входящих
     в группу
    :return:
    """
    if not isinstance(dir_path, Path):
        dir_path = Path(dir_path)

    if not dir_path.exists() or not dir_path.is_dir():
        return

    groups_convert = {ext: group for group, extensions in groups.items() for ext in extensions}

    for file_path in dir_path.iterdir():
        if file_path.is_file() and file_path.suffix[1:] in groups_convert.keys():
            new_dir_path = dir_path / groups_convert[file_path.suffix[1:]]
            if not new_dir_path.exists():
                new_dir_path.mkdir()
            file_path.replace(new_dir_path / file_path.name)
