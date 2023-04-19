def get_int(msg: str) -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError as e:
            print(f"Ошибка: {e}. Повторите ввод")
        finally:
            print("finally")



if __name__ == '__main__':
    i = get_int("Введите целое число: ")
    print(i)
