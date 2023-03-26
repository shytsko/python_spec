from sys import argv

__all__ = ["date_checker"]


def date_checker(date: str) -> bool:
    tokens = date.split('.')
    if len(tokens) != 3 or not all(map(str.isdigit, tokens)):
        return False

    day, month, year = map(int, tokens)

    day_in_month = 31
    if month in (4, 7, 9, 11):
        day_in_month = 30
    elif month == 2:
        day_in_month = 29 if _is_leap_year(year) else 28

    return all((1 <= year <= 9999, 1 <= month <= 12, 1 <= day <= day_in_month))


def _is_leap_year(year: int) -> bool:
    return year % 4 != 0 or year % 100 == 0 and year % 400 != 0


if __name__ == '__main__':
    if len(argv) > 1:
        if date_checker(argv[1]):
            print(f"Строка {argv[1]} является правильной датой")
            exit(0)
        else:
            print(f"Строка {argv[1]} не является правильной датой")
            exit(1)
    else:
        print("Для проверки даты запустите date_tools.py <дата>")
        exit(2)
