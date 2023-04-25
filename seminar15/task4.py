# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году. Логируйте ошибки, если текст не соответсвует формату.
#
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, текущий день
# недели и/или текущий месяц.


from datetime import date, datetime, timedelta
import logging
import argparse


def date_pars(text: str) -> date:
    months = {"января": 1, "февраля": 2, "марта": 3, "апреля": 4, "мая": 5, "июня": 6, "июля": 7, "августа": 8,
              "сентября": 9, "октября": 10, "ноября": 11, "декабря": 12}
    days_week = {"понедельник": 1, "вторник": 2, "среда": 3, "четверг": 4, "пятница": 5, "суббота": 6, "воскресенье": 7}
    week_numbers = {"1-й": 1, "1-я": 1,
                    "2-й": 2, "2-я": 2,
                    "3-й": 3, "3-я": 3,
                    "4-й": 4, "4-я": 4,
                    "5-й": 4, "5-я": 5}

    logger = logging.getLogger(__name__)
    logger.info(f"Получена строка '{text}'")

    try:
        week_num_token, day_token, month_token = text.split()
        week_num = week_numbers[week_num_token]
        day = days_week[day_token]
        month = months[month_token]
    except Exception as e:
        logger.error("Сторка не соответствует формату")
        return None

    return get_date(week_num, day, month)


def get_date(week_num, day, month):
    year = datetime.now().year
    first_day = datetime(year, month, 1)
    while first_day.isoweekday() != day:
        first_day = first_day + timedelta(days=1)

    return first_day + timedelta(days=7 * (week_num - 1))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Определение даты по словесному описанию')
    parser.add_argument('-w', metavar='week', help='Порядковый номер недели', default="1-й")
    parser.add_argument('-d', metavar='day', type=str, help='День недели', default="понедельник")
    parser.add_argument('-m', metavar='month', help='Месяц', default="января")

    logging.basicConfig(filename="task4.log", filemode="w", encoding="utf-8", level=logging.NOTSET)
    # print(date_pars("1-й четверг ноября"))
    # print(date_pars("3-я среда мая"))

    args = parser.parse_args()

    print(args)
