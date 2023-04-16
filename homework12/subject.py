class Subject:
    """
    Информация об успеваимемости по предмету
    """
    def __init__(self, name: str, grade_min: int, grade_max: int, test_result_min: int, test_result_max: int):
        """
        :param name: Название предмета
        :param grade_min: Миниальная допустимая оценка по предмету
        :param grade_max: Максимальная допустимая оценка по предмету
        :param test_result_min: Минимальный допустимый балл за тесты
        :param test_result_max: Максимальный допустимый балл за тесты
        """
        self._name: str = name
        self._grade_min: int = grade_min
        self._grade_max: int = grade_max
        self._test_result_min: int = test_result_min
        self._test_result_max: int = test_result_max
        self._grades: list[int] = []
        self._test_result: list[int] = []

    @property
    def name(self):
        """
        :return: Название предмета
        """
        return self._name

    def add_grade(self, grade: int):
        """
        Добавляет оценку
        :param grade: Оценка
        """
        if grade < self._grade_min or grade > self._grade_max:
            raise ValueError(f"Оценка должна быть от {self._grade_min} до {self._grade_max}")
        self._grades.append(grade)

    def add_test_result(self, test_result: int):
        """
        :param test_result: Результат теста
        """
        if test_result < self._test_result_min or test_result > self._test_result_max:
            raise ValueError(f"Результат теста должен быть от {self._test_result_min} до {self._test_result_max}")
        self._test_result.append(test_result)

    @property
    def grades(self) -> tuple[int]:
        """
        :return: Кортеж из всех оценок
        """
        return tuple(self._grades)

    @property
    def test_results(self) -> tuple[int]:
        """
        :return: Кортеж из всех результатов тестов
        """
        return tuple(self._test_result)

    @property
    def average_grade(self) -> int | float:
        """
        :return: Средняя оценка
        """
        return round(sum(self._grades) / len(self._grades), 2)

    @property
    def average_test_results(self) -> int | float:
        """
        :return: Средний результат по тестам
        """
        return round(sum(self._test_result) / len(self._test_result), 2)
