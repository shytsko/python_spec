# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды

lst = [1, 2, 3, 4, 5, 6, 7, 8, 1, 4, 9, 0, 3, 6, 4, 9, 9, 8]

for item in set(lst):
    if lst.count(item) == 2:
        lst.remove(item)
        lst.remove(item)

print(lst)
