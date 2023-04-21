# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)


from string import ascii_letters, whitespace


def convert_string(source_srting: str) -> str:
    """
    >>> convert_string("this is the test string")
    'this is the test string'
    >>> convert_string("ThIs Is The TEST StRinG")
    'this is the test string'
    >>> convert_string(",,th,is. is t.h/,e... -te./st s-tr,ing")
    'this is the test string'
    >>> convert_string("КПthКпРis is tпрьаhe рtдeэsбавоtип strРогing")
    'this is the test string'
    >>> convert_string("T.hIsЫ IааsаААе87554пррю- The8890 TE,/STа, St,,Riдг3н5nопG!!")
    'this is the test string'
    >>> convert_string(1000)
    Traceback (most recent call last):
    ...
    TypeError: Argument must be a string
    """
    if not isinstance(source_srting, str):
        raise TypeError("Argument must be a string")
    true_chars = ascii_letters + whitespace
    return "".join(c for c in source_srting if c in true_chars).lower()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

