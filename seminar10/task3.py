# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п.
# на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.


class Person:
    def __init__(self, firstname, lastname, age, address):
        self._firstname = firstname
        self._lastname = lastname
        self._age = age
        self._address = address

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f"{self._firstname} {self._firstname}"


if __name__ == '__main__':
    person1 = Person("123", "456", 20, "ggsdgdsgsg")
    print(person1._age)
    person1._age = 30
    print(person1._age)
    person1.birthday()
    print(person1._age)
