# OOP Exercise 1: Create a Class with instance attributes

class Vehical:
    # OOP Exercise 5: Define a property that must have the same value for every class instance (object)
    color = white
    def __init__(self, name, max_speed=0, mileage=0):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name

    # OOP Exercise 3: Create a child class Bus that will inherit all the variables and methods of the Vehicle class
    def ShowVehicalInf(self):
        print(f'Color of Vehical:{self.color}, Vehical Name: {self.name}, Max speed: {self.max_speed}, Mileage: {self.mileage}')

    # OOP Exercise 4: Class Inheritance
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
