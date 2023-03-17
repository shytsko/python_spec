# Функция принимает на вход три списка одинаковой длины:
# имена str,
# ставка int,
# премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

names = ['Vasya', 'Oleg', 'Slavik']
salaries = [60000, 80000, 100000]
premium_rate = ["15.8%", "10.25%", "5.5%"]


def get_premium(names: list[str], salaries: list[int], premium_rate: list[str]) -> dict[str, float]:
    data = zip(names, salaries, map(lambda x: float(x[:-1:]), premium_rate))
    out = {}
    for name, salary, premium in data:
        out[name] = salary * premium / 100
    return out


print(get_premium(names, salaries, premium_rate))
