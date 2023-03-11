# ✔ Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно


def convert(num: int, base: int) -> str:
    symbols: str = "0123456789ABCDEF"
    prefix: set = {2: "0b", 8: "0o", 16: "0x"}

    if base not in prefix:
        return None

    if num == 0:
        return prefix[base] + "0"

    result: str = ""
    if num < 0:
        prefix[base] = "-" + prefix[base]
        num = -num
    while num:
        result = symbols[num % base] + result
        num //= base
    return prefix[base] + result


number = int(input("Введите число: "))
print(f"{number=}, bin={convert(number, 2)}, oct={convert(number, 8)}, hex={convert(number, 16)}")
print(f"{number=}, bin={bin(number)}, oct={oct(number)}, hex={hex(number)}")
