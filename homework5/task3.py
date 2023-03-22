# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).


def fibonacci_generator(count: int) -> int:
    f1, f2 = 1, 1
    counter = 0
    while counter < count:
        counter += 1
        if counter == 1 or counter == 2:
            yield 1
        else:
            f1, f2 = f2, f1 + f2
            yield f2


print(*fibonacci_generator(10))
