import csv
from name import Name
from subject import Subject


class Student:
    first_name = Name()
    last_name = Name()
    SUBJECTS_FILE = "subjects.csv"
    SUBJECTS_HEADER = "subjects"
    GRADE_MIN = 2
    GRADE_MAX = 5
    TESTS_RESULT_MIN = 0
    TESTS_RESULT_MAX = 100

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        with open(self.SUBJECTS_FILE, "r", encoding="UTF-8", newline="") as f:
            reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            header = next(reader)
            if self.SUBJECTS_HEADER in header:
                subjects_col = header.index(self.SUBJECTS_HEADER)
                self._subjects = [Subject(line[subjects_col], self.GRADE_MIN, self.GRADE_MAX,
                                          self.TESTS_RESULT_MIN, self.TESTS_RESULT_MAX)
                                  for line in reader]
            else:
                self._subjects = []

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def subjects(self):
        return tuple((subject.name for subject in self._subjects))

    def __str__(self):
        return self.full_name
