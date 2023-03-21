# ✔ Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт» без перехода на новую строку.


table_part1 = (f"{j:<2} x {i:<2} = {i * j:<2}" for i in range(2, 11) for j in range(2, 6))
table_part2 = (f"{j:<2} x {i:<2} = {i * j:<2}" for i in range(2, 11) for j in range(6, 10))

for _ in range(9):
    print(f"{next(table_part1)}\t{next(table_part1)}\t{next(table_part1)}\t{next(table_part1)}")
print()
for _ in range(9):
    print(f"{next(table_part2)}\t{next(table_part2)}\t{next(table_part2)}\t{next(table_part2)}")
