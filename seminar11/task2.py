# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков архивов
# list-архивы также являются свойствами экземпляра
#
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.


class Archive:
    """
    Класс Архив, хранит пару свойств, число и строку. При создании нового экземпляра класса, старые данные из ранее
    созданных экземпляров сохраняются в пару списков архивов.
    Каждый экземпляр класса хранит данные ранее созданных экземпляров. Более поздние экземпляры не изменяют архивные
    данные более ранних экземпляров
    """
    _last_instance = None

    def __init__(self, str_data: str, int_data: int):
        self._str_data = str_data
        self._int_data = int_data

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        if cls._last_instance:
            instance._str_data_archive = cls._last_instance._str_data_archive.copy() + [cls._last_instance._str_data]
            instance._int_data_archive = cls._last_instance._int_data_archive.copy() + [cls._last_instance._int_data]
        else:
            instance._str_data_archive = []
            instance._int_data_archive = []
        cls._last_instance = instance
        return instance

    def __str__(self):
        return f"Архив. Текущие данные:" \
               f"\tstr_data = {self._str_data}; int_data = {self._int_data}\n" \
               f"Архивные данные:\n" \
               f"\tstr_data_archive = {self._str_data_archive}\n" \
               f"\tint_data_archive = {self._int_data_archive}"

    def __repr__(self):
        return f"Archive({self._str_data}, {self._int_data})"


if __name__ == '__main__':
    archive_1 = Archive("str1", 1)
    archive_2 = Archive("str2", 2)
    archive_3 = Archive("str3", 3)
    print(archive_1)
    print(archive_2)
    print(archive_3)
    # help(Archive)
    archive_list = [archive_1, archive_2, archive_3]
    print(archive_list)
