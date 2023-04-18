# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или
# вещественное число. Обрабатывайте не числовые данные как исключения.


def get_number(msg: str) -> int | float:
    while True:
        num = input(msg)
        try:
            return int(num)
        except ValueError as e:
            try:
                return float(num)
            except ValueError as e:
                print("Не верный ввод. Повторите")


if __name__ == '__main__':
    print(get_number("Введите целое или вещественное число: "))
