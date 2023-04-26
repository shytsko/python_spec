from pathlib import Path

__all__ = ["files_rename"]


def files_rename(dir_path: Path | str, *, extensions: list[str], new_extension: str,
                 old_name_range: tuple[int, int] = (0, 0), new_name: str = "~", counter_len: int = 3) -> None:
    """
    Переименовывает файлы с указанными расширениями
    :param dir_path: Каталог с файлами
    :param extensions: Список с расширениями файлов, которые нужно переименовать
    :param new_extension: Новое расширение для всех файлов
    :param old_name_range: Диапазон индексов символов из старого имени. которые нужно оставить
    :param new_name: Новое имя
    :param counter_len: Количество знаков счетчика файлов
    :return:
    """
    if not isinstance(dir_path, Path):
        dir_path = Path(dir_path)

    if not dir_path.exists() or not dir_path.is_dir():
        return

    file_counter = 1
    for file_path in dir_path.iterdir():
        if file_path.is_file() and file_path.suffix[1:] in extensions:
            new_file_name = file_path.stem if old_name_range[1] == 0 else file_path.stem[
                                                                          old_name_range[0]:old_name_range[1]]
            new_file_name += f"{new_name}{file_counter:0>{counter_len}}.{new_extension}"
            file_path.rename(file_path.with_name(new_file_name))
            file_counter += 1
