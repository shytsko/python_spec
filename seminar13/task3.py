# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class UserError(Exception):
    pass


class UserLevelError(UserError):
    def __init__(self, required_level, user_level):
        self._required_level = required_level
        self._user_level = user_level

    def __str__(self):
        return f"User level error. Level {self._required_level} required, user level {self._user_level}"


class UserAccessError(UserError):
    def __init__(self, login: str, id_: int):
        self._login = login
        self._id = id_

    def __str__(self):
        return f"User access error. The user with the name {self._login} and id {self._id} does not exist"


if __name__ == '__main__':
    raise UserAccessError
