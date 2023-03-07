# Напишите программу, которая запрашивает год и проверяет его
# на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

YEAR_START = 1582

year = int(input("Введите год: "))
message = ""

if year < YEAR_START or year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    message = f"Год {year} не високосный"
else:
    message = f"Год {year} високосный"

print(message)
