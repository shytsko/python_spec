# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from pathlib import Path
from task4 import file_generator_ex


def files_sorting(dir_path: Path | str, groups: dict[str, list[str]]) -> None:
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


if __name__ == '__main__':
    file_generator_ex("task7", img=3, png=4, jpg=5, avi=4, mk4=9, py=1, html=5, txt=6, md=2)
    files_sorting("task7", {"image": ["img", "png", "jpg"], "video": ["avi", "mk4"], "src": ["py", "html"]})
