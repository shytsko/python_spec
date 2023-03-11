# ✔ Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять не менее 42 знаков после запятой.
import decimal

decimal.getcontext().prec = 42

PI = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')

diameter: decimal.Decimal = decimal.Decimal(input("Enter the diameter (no more than 1000): "))

if 0 <= diameter <= 1000:
    circle_length = PI * diameter
    circle_area = PI * (diameter / 2) ** 2
    print(f"{circle_area=} {circle_length=}")
else:
    print("Incorrect diameter value")

