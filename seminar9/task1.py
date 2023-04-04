# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from random import randint
from typing import Callable

NUM_MIN = 1
NUM_MAX = 100
TRIES_MIN = 1
TRIES_MAX = 10


def check_arguments(func):
    def wrapper(secret, num_tries, *args, **kwargs):
        if secret < NUM_MIN or secret > NUM_MAX:
            secret = randint(NUM_MIN, NUM_MAX)
        if num_tries < TRIES_MIN or num_tries > TRIES_MAX:
            num_tries = randint(TRIES_MIN, TRIES_MAX)
        return func(secret, num_tries, *args, **kwargs)

    return wrapper


@check_arguments
def guessing_game(secret: int, num_tries) -> Callable[[int], tuple[bool, int]]:
    print(f"Угадайте число {secret} за {num_tries} попыток")

    def game_fun(user_num: int) -> tuple[bool, int]:
        nonlocal num_tries, secret
        if user_num == secret:
            return True, 0
        num_tries -= 1

        return False, num_tries

    return game_fun


game = guessing_game(555, 5)
while True:
    num = int(input("Введите число: "))
    res, tries = game(num)
    if res:
        print("Вы угадали!!")
        break
    if tries == 0:
        print("Попыток больше нет")
        break
    print(f"Осталось попыток: {tries}")
