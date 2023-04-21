Тест функции
===

>>> from doc_test import check_year

>>> check_year(2023)
False

>>> check_year(1900)
False

>>> check_year(2000)
True

>>> check_year(1982)
False

>>> check_year(1984)
True

>>> check_year(1984.0)
Traceback (most recent call last):
...
TypeError: Argument year=1984.0 is not of a valid type. Argument must be of type int