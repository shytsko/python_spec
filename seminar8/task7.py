# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.
import csv
import pickle
from pprint import pprint

if __name__ == '__main__':
    with open("task6.csv", "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        data = [line for line in reader]

    pprint(data)
    print(pickle.dumps(data))
