"""
Розробіть клас Vehicle для представлення транспортного засобу.
Додайте атрибути, такі як назва, швидкість і вартість.
Реалізуйте метод __gt__, який порівнює два транспортних засоби за швидкістю.
Створіть список транспортних засобів і відсортуйте його за швидкістю
"""


class Vehicle:
    def __init__(self, name, speed, cost):
        self.name = name
        self.speed = speed
        self.cost = cost

    def __gt__(self, other):
        return self.speed < other.speed


vehicle1 = Vehicle("Car", 150, 30000)
vehicle2 = Vehicle("Bike", 25, 500)
vehicle3 = Vehicle("Train", 200, 1000000)

vehicles = [vehicle1, vehicle2, vehicle3]

sorted_vehicles_speed = vehicles.sort(reverse=True)

for vehicle in vehicles:
    print(f"Vehicle: {vehicle.name}, Speed: {vehicle.speed}, Cost: {vehicle.cost}")