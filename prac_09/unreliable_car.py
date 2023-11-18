from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Represent an UnreliableCar object."""

    def __init__(self, name, fuel, reliability):
        """Inisialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive a car given a distance and reliability score."""
        if self.reliability < randint(1, 100):
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven




