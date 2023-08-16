"""
Створіть клас Rectangle для представлення прямокутника.
Додайте методи для обчислення площі та периметра прямокутника.
Створіть об'єкт Rectangle і викличте ці методи.
"""


class Rectangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def perimetr(self):
        return 2 * self.base + 2 * self.height

    def area(self):
        return self.base * self.height


rectangle = Rectangle(4, 5)

print(f"Площа вашого прямокутника: {Rectangle.area(rectangle)}")
print(f"Периметр вашого прямокутника: {Rectangle.perimetr(rectangle)}")