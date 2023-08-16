"""
Створіть клас Circle, який представляє коло.
Реалізуйте методи для обчислення площі та довжини кола.
Використовуйте аттрибут класу для зберігання значення π (pi).
"""
import math


class Circle:
    pi_number = math.pi

    def __init__(self, radius):
        self.radius = radius

    def length_of_circle(self):
        return round(2 * self.pi_number * self.radius, 2)
    
    def area_of_circle(self):
        return round(self.pi_number * self.radius ** 2, 2)


circle = Circle(5)

print(f"Area of the circle: {circle.area_of_circle()}")
print(f"Length of the circle: {circle.length_of_circle()}")
