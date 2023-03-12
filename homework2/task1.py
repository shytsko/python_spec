# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def convert(num: int, base: int) -> str:
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUV"
    prefixes = {2: "0b", 8: "0o", 16: "0x"}

    if not (2 <= base <= 32):
        return None

    prefix = prefixes[base] if base in prefixes else f"{base}'"

    if num == 0:
        return prefix + "0"

    result: str = ""
    if num < 0:
        prefix = "-" + prefix
        num = -num
    while num:
        result = symbols[num % base] + result
        num //= base
    return prefix + result


number = int(input("Введите число: "))
print(f"{number=}, bin={convert(number, 2)}, oct={convert(number, 8)}, hex={convert(number, 16)}, "
      f"in 32 base {convert(number, 32)}, in 5 base {convert(number, 5)}")
print(f"{number=}, bin={bin(number)}, oct={oct(number)}, hex={hex(number)}")
