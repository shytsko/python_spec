#  Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔ второе и третье число являются ключами.
# ✔ первое число является значением для первого ключа.
# ✔ четвертое и все возможные последующие числа  хранятся в кортеже как значения второго ключа.


text = '45/57/76/33/78/4/90'

a, b, c, *d = map(int, text.split("/"))

out = {b: a, c: tuple(d)}

print(out)