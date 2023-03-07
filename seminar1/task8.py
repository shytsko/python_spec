# Нарисовать в консоли ёлку спросив у пользователя количество
# рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

CHAR = "*"
SPACE = " "
rows = int(input("Сколько рядов у ёлки? "))

for row in range(rows):
    for _ in range(rows - row - 1):
        print(SPACE, end="")
    for _ in range(row * 2 + 1):
        print(CHAR, end="")
    print()
