# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре
#   недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов
#   вместе взятых.
from student import Student
from random import randint, choice

COUNT_GRADES = 30
COUNT_TESTS = 50

if __name__ == '__main__':
    student = Student("Иван", "Иванович", "Иванов")
    for _ in range(COUNT_GRADES):
        student.add_grade(choice(student.subjects), randint(Student.GRADE_MIN, Student.GRADE_MAX))
    for _ in range(COUNT_TESTS):
        student.add_test_result(choice(student.subjects), randint(Student.TEST_RESULT_MIN, Student.TEST_RESULT_MAX))
    print(student)
