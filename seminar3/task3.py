# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где
# ключ - тип элемента,
# значение - список элементов данного типа.

data = (
5, 6.54, "54568", (44, 77), True, None, ["ffdg", 55, 2], {4, 2, 7, 9, 2}, "jyfggdhdhtht", ["dfdgdsf", "sdffdgd"])

dict_types = dict()

for item in data:
    list_items = dict_types.setdefault(type(item), [])
    list_items.append(item)

print(dict_types)
