# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
import random

from task3 import Person


class Employee(Person):
    __level_factor = 7

    def __init__(self, id_num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._id = id_num if 100_000 <= id_num <= 999_999 else random.randint(100_000, 999_999)

    def get_level(self) -> int:
        return sum(map(int, str(self._id))) % self.__level_factor


if __name__ == '__main__':
    employee = Employee(100_000, "123", "456", 20, "ggsdgdsgsg")
    print(employee.get_level())
