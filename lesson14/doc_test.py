YEAR_START = 1582


def check_year(year):
    """
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
    """
    return not (year < YEAR_START or year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


if __name__ == '__main__':
    import doctest
    # doctest.testmod(verbose=True)
    doctest.testfile("test.md", verbose=True)