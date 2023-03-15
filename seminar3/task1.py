# ✔ Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходнёёого списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.


source_list = [5, 3, 8, 0, 5, 2, 0, 5, 2, 4, 8]

unique_list1 = list(set(source_list))
print(unique_list1)

unique_list2 = []
for item in source_list:
    if item not in unique_list2:
        unique_list2.append(item)

print(unique_list2)
