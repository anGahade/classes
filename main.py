"""
Створіть клас Student для представлення студента.
Додайте атрибути, такі як ім'я, прізвище і список оцінок.
Реалізуйте метод __len__, який повертає кількість оцінок студента.
Створіть список студентів і відсортуйте його за кількістю оцінок.
"""


class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = list(marks)

    def __len__(self):
        return len(self.marks)

    def __lt__(self, other):
        return len(self) < len(other)


student_1 = Student("Alex", "Jackson", [1, 5, 23, 16])
student_2 = Student("Sonia", "Hellman", [23, 76, 16])
student_3 = Student("Cristin", "Rubinstein", [1, 5, 23, 76, 16])

stud_list = [student_1, student_2, student_3]
stud_marks_sort = sorted(stud_list)

for student in stud_marks_sort:
    print(f"Student: {student.name} {student.surname}, Number of Marks: {len(student)}")
