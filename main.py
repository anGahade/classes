"""
Створіть клас Student, який представляє студента.
Реалізуйте атрибут класу для відстеження кількості студентів.
Для цього змінюйте значення атрибуту класу у методі __init__ .
Та створіть клас метод для виведення загальної кількості студентів.
"""


class Student:

    total_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.total_students += 1

    @classmethod
    def display_students(cls):
        print(f"Загальна кількість студентів {cls.total_students}")


student1 = Student("Alice", 20)
student2 = Student("Jack", 23)
student3 = Student("Tom", 26)
student4 = Student("Hellen", 19)

Student.display_students()