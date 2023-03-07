# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

MIN_VALUE = 1
MAX_VALUE = 999
MAX_SINGLE = 9
MAX_TWO_DIGIT = 99

repeat = True

while repeat:
    value = int(input("Введите число: "))
    if MIN_VALUE < value < MAX_VALUE:
        repeat = False
        if value <= MAX_SINGLE:
            message = str(value ** 2)
        elif value <= MAX_TWO_DIGIT:
            message = str(value // 10 + value % 10)
        else:
            message = str(value // 100 + value // 10 % 10 * 10 + value % 10 * 100)
    else:
        message = "Повторите ввод!"
    print(message)
