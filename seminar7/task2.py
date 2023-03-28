# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import randint, choice, shuffle
from string import ascii_lowercase

MIN_LEN = 4
MAX_LEN = 7
VOWELS = 'aeijou'


def get_alias(file_name, count) -> str:
    with open(file_name, 'a', encoding='utf-8') as f:

        for _ in range(count) :
            alias_len = randint(MIN_LEN, MAX_LEN)
            alias_chars = [choice(VOWELS)]

            for i in range(alias_len - 1):
                alias_chars.append(choice(ascii_lowercase))
            shuffle(alias_chars)

            alias = "".join(alias_chars).capitalize()

            print(alias, file=f)


if __name__ == '__main__':
    get_alias("alias.txt", 10)
