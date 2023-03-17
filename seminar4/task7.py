# ✔ Функция получает на вход словарь с названием компании в качестве ключа и
# списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании.
# Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

companies_data = {
    "Sun": [100000, 5050600, -456000, 80000, -90500],
    "MicroSoft": [200600, -666666, 706500, -900000, 1000000],
    "Yandex": [50000, 60600, -94500]
}


def is_all_profitable(companies: dict[str, list[int]]) -> bool:
    profit = {}
    for name, income_expenses in companies.items():
        profit[name] = sum(income_expenses)

    return all(map(lambda x: x[1] > 0, profit.items()))


print(is_all_profitable(companies_data))
