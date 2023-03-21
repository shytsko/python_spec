# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило: «число является простым, если делится
# нацело только на единицу и на себя»

def prime_numbers_generator(count: int) -> int:
    current = 1
    counter = 0
    while counter < count:
        current += 1
        if is_prime(current):
            counter += 1
            yield current


def is_prime(num: int) -> bool:
    if num % 2 == 0:
        return num == 2
    div = 3
    while div * div <= num and num % div != 0:
        div += 2
    return div * div > num


prime_numbers = prime_numbers_generator(100)
print(*prime_numbers)
