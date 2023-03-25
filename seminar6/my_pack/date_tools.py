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
