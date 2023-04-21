import doctest
import unittest
import doc_test


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(doc_test))
    tests.addTests(doctest.DocFileSuite('test.md'))
    return tests


if __name__ == '__main__':
    unittest.main()
