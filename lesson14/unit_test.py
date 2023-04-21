import unittest
from doc_test import check_year


class TestCheckYear(unittest.TestCase):
    def test_true(self):
        self.assertTrue(check_year(2000))
        self.assertTrue(check_year(1984))

    def test_false(self):
        self.assertFalse(check_year(2023))
        self.assertFalse(check_year(1900))
        self.assertFalse(check_year(1982))
        self.assertFalse(check_year(1500))
        self.assertFalse(check_year(1200))

    def test_type(self):
        with self.assertRaises(TypeError):
            x = check_year("1200")
            # x = check_year(1200.0)


if __name__ == '__main__':
    unittest.main(verbosity=3)
