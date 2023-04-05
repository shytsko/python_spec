# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

import csv
import json
from pathlib import Path
from random import randint

MIN_ROWS = 100
MAX_ROWS = 1000
MIN_COEF = -1000
MAX_COEF = 1000
CSV_FILE_NAME = "coefficients.csv"
JSON_FILE_NAME = "results.json"


def create_csv(file_name):
    count_rows = randint(MIN_ROWS, MAX_ROWS)
    with open(file_name, "w", encoding="UTF-8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(["a", "b", "c"])
        for _ in range(count_rows):
            writer.writerow([randint(MIN_COEF, MAX_COEF), randint(MIN_COEF, MAX_COEF), randint(MIN_COEF, MAX_COEF)])


def solve_all_from_csv(func):
    def wrapper(*args, **kwargs):
        create_csv(CSV_FILE_NAME)
        with open(CSV_FILE_NAME, "r", encoding="UTF-8", newline="") as f:
            reader = csv.DictReader(f, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                func(**row)
        return func(*args, **kwargs)

    return wrapper


def save_to_json(func):
    def wrapper(*args, **kwargs):
        file = Path(JSON_FILE_NAME)
        if file.exists():
            with file.open("r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = []
        res = func(*args, **kwargs)
        data.append({"args": [*args], **kwargs, "res": str(res)})
        with open(JSON_FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return res

    return wrapper


@solve_all_from_csv
@save_to_json
def quadratic_equation_solution(a, b, c):
    d = b ** 2 - 4 * a * c

    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)

    return x1, x2


if __name__ == '__main__':
    print(quadratic_equation_solution(4, 6, 0))
