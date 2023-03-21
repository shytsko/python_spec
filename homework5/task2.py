# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии


names = ['Vasya', 'Oleg', 'Slavik']
salaries = [60000, 80000, 100000]
premium_rate = ["15.8%", "10.25%", "5.5%"]

premium = {name: salary * premium / 100 for name, salary, premium in
           zip(names, salaries, map(lambda x: float(x[:-1:]), premium_rate))}

print(premium)
