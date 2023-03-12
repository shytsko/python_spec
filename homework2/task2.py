# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions.
import math
import fractions


def input_fraction(message: str) -> tuple:
    input_text = input(message).split("/")
    if len(input_text) == 2 and input_text[0].isdigit() and input_text[1].isdigit():
        return int(input_text[0]), int(input_text[1])
    return None


def fraction_to_str(fraction: tuple) -> str:
    return f"{fraction[0]}/{fraction[1]}"


def addition_fraction(fraction1: tuple, fraction2: tuple) -> tuple:
    lcm = math.lcm(fraction1[1], fraction2[1])
    return fraction1[0] * (lcm // fraction1[1]) + fraction2[0] * (lcm // fraction2[1]), lcm


def multiplication_fractions(fraction1: tuple, fraction2: tuple) -> tuple:
    numerator = fraction1[0] * fraction2[0]
    denominator = fraction1[1] * fraction2[1]
    gcd = math.gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd


fraction1 = input_fraction("Введите первую дробь: ")
fraction2 = input_fraction("Введите вторую дробь: ")

if fraction1 is not None and fraction2 is not None:
    print(f"fraction1={fraction_to_str(fraction1)}, fraction2={fraction_to_str(fraction2)}")
    sum_fraction = addition_fraction(fraction1, fraction2)
    print(f"sum_fraction={fraction_to_str(sum_fraction)}")
    mult_fraction = multiplication_fractions(fraction1, fraction2)
    print(f"mult_fraction={fraction_to_str(mult_fraction)}")

    test_fraction1 = fractions.Fraction(fraction1[0], fraction1[1])
    test_fraction2 = fractions.Fraction(fraction2[0], fraction2[1])
    print(f"Test: addition {test_fraction1 + test_fraction2}, "
          f"multiplication {test_fraction1 * test_fraction2}")
else:
    print("Некорректный ввод")
