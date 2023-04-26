# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году. Логируйте ошибки, если текст не соответсвует формату.
#
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, текущий день
# недели и/или текущий месяц.


from datetime import date, datetime, timedelta
import logging
import argparse

MONTHS = {"января": 1, "февраля": 2, "марта": 3, "апреля": 4, "мая": 5, "июня": 6, "июля": 7, "августа": 8,
          "сентября": 9, "октября": 10, "ноября": 11, "декабря": 12}
DAYS_WEEK = {"понедельник": 1, "вторник": 2, "среда": 3, "четверг": 4, "пятница": 5, "суббота": 6, "воскресенье": 7}
logger = logging.getLogger(__name__)


def date_parse(text: str) -> date:
    logger.info(f"Получена строка '{text}'")

    try:
        week_num_token, day_token, month_token = text.split()
        week_num = int(week_num_token[0])
        day = DAYS_WEEK[day_token]
        month = MONTHS[month_token]
    except (ValueError, KeyError):
        logger.error("Строка не соответствует формату")
        return None

    return get_date(week_num, day, month)


def get_date(week_num, day, month):
    year = datetime.now().year
    first_day = datetime(year, month, 1)
    while first_day.isoweekday() != day:
        first_day = first_day + timedelta(days=1)

    search_date = first_day + timedelta(days=7 * (week_num - 1))

    if search_date.month == month:
        logger.info(f"Дата: {search_date}")
        return search_date
    else:
        logger.warning("Такой даты не существует")
        return None


def int_or_str(text):
    try:
        return int(text)
    except ValueError:
        return text


def parse_arguments():
    parser = argparse.ArgumentParser(description='Определение даты по заданным параметрам')
    parser.add_argument('-w', metavar='week', type=int_or_str, help='Порядковый номер недели', default=1)
    parser.add_argument('-d', metavar='day', type=int_or_str, help='День недели', default=datetime.now().isoweekday())
    parser.add_argument('-m', metavar='month', type=int_or_str, help='Месяц', default=datetime.now().month)

    args = parser.parse_args()

    try:
        day = args.d if not isinstance(args.d, int) else list(DAYS_WEEK.keys())[args.d - 1]
        month = args.m if not isinstance(args.m, int) else list(MONTHS.keys())[args.m - 1]
    except IndexError:
        logger.error(f"Переданы не правильные параметры: {args}")
    else:
        return date_parse(f"{args.w} {day} {month}")


if __name__ == '__main__':
    logging.basicConfig(filename="task4.log", filemode="w", encoding="utf-8", level=logging.NOTSET)

    print(date_parse("1-й четверг ноября"))
    print(date_parse("3-я среда мая"))
    print(parse_arguments())
