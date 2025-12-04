class Vehicle:
    def max_speed(self):
        return 0

class Car(Vehicle):
    def max_speed(self):
        return 180

class Bike(Vehicle):
    def max_speed(self):
        return 120

c=Car()
print("Car's max speed: ", c.max_speed())

b=Bike()
print("Bike's max speed: ", b.max_speed())