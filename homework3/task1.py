# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

source_list = [5, 3, 8, 0, 5, 2, 0, 5, 2, 4, 8]

duplicate_list = [x for x in set(source_list) if source_list.count(x) > 1]

print(f"Source list: {source_list}\nDublicate items: {duplicate_list}")
