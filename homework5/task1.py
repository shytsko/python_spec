# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def path_parser(path: str) -> tuple[str, str, str]:
    route, file = path.rsplit('\\', maxsplit=1)
    file_name, file_extension = file.rsplit('.', maxsplit=1)
    return route, file_name, file_extension


print(path_parser(r"D:\Documents\GB\python_spec\homework5\task1.py"))
