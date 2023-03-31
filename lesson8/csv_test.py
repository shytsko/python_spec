import csv
from pprint import pprint

# with (
#     open("data.csv", 'r', newline='') as f,
#     open("new_data.csv", 'w', newline='', encoding='utf-8') as f_w
# ):
#     csv_reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
#     csv_writer = csv.writer(f_w, dialect='excel-tab', quoting=csv.QUOTE_MINIMAL, delimiter=' ', quotechar='|')
#     for line in csv_reader:
#         csv_writer.writerow(line)

# with open("data.csv", 'r', newline='') as f:
#     csv_dict = csv.DictReader(f)
#     for row in csv_dict:
#         print(row)

rows = [
    {"a": "a1", "b": "b1", "c": "c1", "d": "d1"},
    {"a": "a2", "b": "b2", "d": "d2"},
    {"a": "a3", "b": "b3", "c": "c3"},
    {"b": "a4", "c": "c4", "d": "d4", "e": "e4", "f": "f4"}
]

with open("dict_write.csv", "w", encoding="utf-8", newline="") as f:
    csv_write = csv.DictWriter(f, fieldnames=["a", "c", "b", "d"], restval="Empty", extrasaction="ignore")
    csv_write.writeheader()
    csv_write.writerows(rows)
