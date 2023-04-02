# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.

import json
import csv


def convert_users_data_to_csv(input_csv: str, output_json: str) -> None:
    with open(input_csv, "r", encoding="utf-8", newline="") as f:
        csv_rows = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        headers = csv_rows.__next__()
        for i, header in enumerate(headers):
            if header == "id":
                id_col = i
            elif header == "name":
                name_col = i
            elif header == "level":
                level_col = i

        data = []
        for row in csv_rows:
            data.append({
                "id": f"{int(row[id_col]):0>10}",
                "name": row[name_col].capitalize(),
                "level": int(row[level_col]),
                "hash": hash((row[id_col], row[name_col]))
            })

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    convert_users_data_to_csv("task3.csv", "task4.json")
