import csv
from name import Name
from subject import Subject


class Student:
    """
    Информация о студенте
    """
    first_name = Name()
    middle_name = Name()
    last_name = Name()
    SUBJECTS_FILE = "subjects.csv"
    SUBJECTS_HEADER = "subjects"
    GRADE_MIN = 2
    GRADE_MAX = 5
    TEST_RESULT_MIN = 0
    TEST_RESULT_MAX = 100
    ROUND_NUM = 2

    def __init__(self, first_name: str, middle_name: str, last_name: str):
        """
        :param first_name: Имя
        :param middle_name: Отчество
        :param last_name: Фамилия
        """
        self.first_name: str = first_name
        self.middle_name: str = middle_name
        self.last_name: str = last_name
        self._subjects: dict[str, Subject] = {}
        with open(self.SUBJECTS_FILE, "r", encoding="UTF-8", newline="") as f:
            reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            header = next(reader)
            if self.SUBJECTS_HEADER in header:
                subjects_col = header.index(self.SUBJECTS_HEADER)
                self._subjects.update({line[subjects_col]: Subject(line[subjects_col],
                                                                   self.GRADE_MIN,
                                                                   self.GRADE_MAX,
                                                                   self.TEST_RESULT_MIN,
                                                                   self.TEST_RESULT_MAX)
                                       for line in reader})

    @property
    def full_name(self) -> str:
        """
        :return: Полное имя
        """
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    @property
    def subjects(self) -> tuple[str]:
        """
        :return: Кортеж из названий предметов
        """
        return tuple(self._subjects.keys())

    def add_grade(self, subject_name: str, grade: int):
        """
        Добавляет оценку по предмету
        :param subject_name: Название предмета
        :param grade: Оценка
        """
        self._validate_subject(subject_name)
        self._subjects[subject_name].add_grade(grade)

    def add_test_result(self, subject_name: str, test_result: int):
        """
        Добавляет результат теста по предмету
        :param subject_name: Название предмета
        :param test_result: Баллы по тесту
        """
        self._validate_subject(subject_name)
        self._subjects[subject_name].add_test_result(test_result)

    def get_average_test_result(self, subject_name) -> int | float:
        """
        :param subject_name: Название предмета
        :return: Средний результат тестов по предмету
        """
        self._validate_subject(subject_name)
        return self._subjects[subject_name].average_test_results

    def get_average_grade_all(self) -> int | float:
        """
        :return: Средняя оценка по всем предметам
        """
        sum_grades = 0
        count_grades = 0
        for subject in self._subjects.values():
            sum_grades += sum(subject.grades)
            count_grades += len(subject.grades)
        return round(sum_grades / count_grades, self.ROUND_NUM)

    def _validate_subject(self, subject_name):
        if subject_name not in self._subjects:
            raise ValueError(f"Название предмета должно быть из {self.subjects}")

    def __str__(self):
        res = [f"Студент: {self.full_name}\n", "------------------------------\n"]

        for subject_name, subject in self._subjects.items():
            res.append(
                f"Предмет: {subject_name}\n"
                f"Результаты тестов: {', '.join(map(str, self._subjects[subject_name].test_results))}. "
                f"Средний балл: {self.get_average_test_result(subject_name)}\n"
                f"Оценки: {', '.join(map(str, self._subjects[subject_name].grades))}.\n"
                f"------------------------------\n")
        res.append(f"Средняя оценка по всем предметам: {self.get_average_grade_all()}\n")
        return "".join(res)
