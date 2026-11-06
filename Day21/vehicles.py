class Vehicle:
    def describe(self):
        print("This is a vehicle")


class Car(Vehicle):
    def describe(self):
        print("This is a Car")


class Bike(Vehicle):
    def describe(self):
        print("This is a Bike")


car1 = Car()
bike1 = Bike()

car1.describe()
bike1.describe()