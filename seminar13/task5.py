# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
import json
from task4 import User
from task3 import UserAccessError, UserLevelError


class Project:
    def __init__(self, users_file_name):
        self._users = self.load_users(users_file_name)

    def load_users(self, file_name) -> set[User]:
        with open(file_name, "r", encoding="UTF-8") as f:
            json_data = json.load(f)
        return {User(int(id_), name, int(level)) for level, users in json_data.items() for id_, name in users.items()}

    def login(self, login: str, id_: int):
        login_user = User(id_, login)
        for user in self._users:
            if user == login_user:
                return user.level
        raise UserAccessError(login, id_)

    def add_user(self, login: str, id_: int, new_user: User):
        my_level = self.login(login, id_)
        if new_user.level < my_level:
            raise UserLevelError(new_user.level, my_level)
        self._users.add(new_user)

    def __str__(self):
        return str(self._users)


if __name__ == '__main__':
    project = Project("../seminar8/task2.json")
    my_name = "bill"
    my_id = 66
    project.add_user(my_name, my_id, User(10, "new_user", 5))
    print(project)

