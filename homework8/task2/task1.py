# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдоименами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.
import json

__all__ = ["convert_file"]


def convert_file(txt_file_name, json_file_name):
    with open(txt_file_name, "r", encoding="utf-8") as f:
        lines = list(f)
    data = {"data": {}}

    for line in lines:
        key, value = line[:-1].split("|")
        key = key.capitalize()
        if value.isdigit():
            value = int(value)
        else:
            value = float(value)
        data["data"][key] = value

    with open(json_file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


if __name__ == '__main__':
    convert_file("../seminar7/result.txt", "task1.json")
