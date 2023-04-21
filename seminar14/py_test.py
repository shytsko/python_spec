# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from task1 import convert_string
import pytest


def test_without_changes():
    assert convert_string("this is the test string") == "this is the test string"


def test_fix_case():
    assert convert_string("ThIs Is The TEST StRinG") == "this is the test string"


def test_fix_punctuation():
    assert convert_string("this is.. ,,the te,,s...t st-r-ing") == "this is the test string"


def test_fix_other_letter():
    assert convert_string("КПthКпРis is tпрьаhe рtдeэsбавоtип strРогing") == "this is the test string"


def test_fix_all():
    assert convert_string("T.hIsЫ IааsаААе87554пррю- The8890 TE,/STа, St,,Riдг3н5nопG!!") == "this is the test string"


def test_type():
    with pytest.raises(TypeError, match="Argument must be a string"):
        convert_string(1000)


if __name__ == '__main__':
    pytest.main(['-v'])
