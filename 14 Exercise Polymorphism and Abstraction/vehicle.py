from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        ...

    @abstractmethod
    def refuel(self, fuel):
        ...


class Car(Vehicle):
    CONDITIONER_ON = 0.9

    def drive(self, distance):
        if self.fuel_quantity > (self.fuel_consumption + Car.CONDITIONER_ON) * distance:
            self.fuel_quantity -= (self.fuel_consumption + Car.CONDITIONER_ON) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER_ON = 1.6

    def drive(self, distance):
        if self.fuel_quantity * 0.95 > (self.fuel_consumption + Truck.CONDITIONER_ON) * distance:
            self.fuel_quantity -= (self.fuel_consumption + Truck.CONDITIONER_ON) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

