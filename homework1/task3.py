# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна
# подсказывать “больше” или “меньше” после каждой попытки.

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPT_AVAILABLE = 10

secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)

attempts_left = ATTEMPT_AVAILABLE

while attempts_left > 0:
    number = int(input(f"Отгадайте число (осталось попыток: {attempts_left}): "))
    if number == secret_number:
        print("Вы угадали!!!")
        break
    elif secret_number > number:
        print("Загадонное числое больше вашего.")
    else:
        print("Загадонное числое меньше вашего.")
    attempts_left -= 1
else:
    print(f"Попыток больше нет. Было загадано число {secret_number}.")
