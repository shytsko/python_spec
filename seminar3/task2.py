# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# целое положительное число
# вещественное положительное или отрицательное число
# строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# строку в верхнем регистре в остальных случаях


input_text = input("Введите строку: ")

if input_text.isdigit():
    int_data = int(input_text)
    print(f"{int_data=}")
elif input_text.removeprefix("-").replace(".", "", 1).isdigit():
    float_data = float(input_text)
    print(f"{float_data = }")
elif input_text.lower() != input_text:
    lower_data = input_text.lower()
    print(f"{lower_data=}")
else:
    upper_data = input_text.upper()
    print(f"{upper_data=}")
