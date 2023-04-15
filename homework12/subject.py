class Subject:
    def __init__(self, name, grade_min, grade_max, test_result_min, test_result_max):
        self._name = name
        self._grade_min = grade_min
        self._grade_max = grade_max
        self._test_result_min = test_result_min
        self._test_result_max = test_result_max
        self._grades = []
        self._test_result = []

    @property
    def name(self):
        return self._name

    def add_grade(self, grade):
        if grade < self._grade_min or grade > self._grade_max:
            raise ValueError(f"Subject grade should be from {self._grade_min} to {self._grade_max}")
        self._grades.append(grade)

    def add_test_result(self, test_result):
        if test_result < self._test_result_min or test_result > self._test_result_max:
            raise ValueError(f"Subject test result should be from {self._test_result_min} to {self._test_result_max}")
        self._test_result.append(test_result)

    @property
    def grades(self):
        return tuple(self._grades)

    @property
    def test_results(self):
        return tuple(self._test_result)

    @property
    def average_grade(self):
        return round(sum(self._grades) / len(self._grades), 2)

    @property
    def average_test_results(self):
        return round(sum(self._test_result) / len(self._test_result), 2)
