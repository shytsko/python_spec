# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from task1 import convert_string
import unittest


class TestConvertString(unittest.TestCase):

    def test_without_changes(self):
        self.assertEqual(convert_string("this is the test string"), "this is the test string")

    def test_fix_case(self):
        self.assertEqual(convert_string("ThIs Is The TEST StRinG"), "this is the test string")

    def test_fix_punctuation(self):
        self.assertEqual(convert_string("this is.. ,,the te,,s...t st-r-ing"), "this is the test string")

    def test_fix_other_letter(self):
        self.assertEqual(convert_string("КПthКпРis is tпрьаhe рtдeэsбавоtип strРогing"), "this is the test string")

    def test_fix_all(self):
        self.assertEqual(convert_string("T.hIsЫ IааsаААе87554пррю- The8890 TE,/STа, St,,Riдг3н5nопG!!"),
                         "this is the test string")

    def test_type(self):
        self.assertRaisesRegex(TypeError, "Argument must be a string", convert_string, 1000)


if __name__ == '__main__':
    unittest.main(verbosity=2)
