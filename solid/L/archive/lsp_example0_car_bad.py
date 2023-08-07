_ = """
LSP: Bad Example
"""
#%%

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, name: str):
        self._name = name
        self._speed = 0
        self._gears = ["N", "1", "2", "3", "4", "5", "6", "R"]
        self._gear = "N"

    @abstractmethod
    def change_gear(self, gear: str):
        pass

    @abstractmethod
    def accelerate(self):
        pass


class Bicycle(Vehicle):
    pass


class Car(Vehicle):
    def __init__(self, name: str):
        super().__init__(name)

    def change_gear(self, gear: str):
        if gear in self._gears:
            self.gear = gear
            print(f"Car {self._name} is in gear {self.gear}")

    def accelerate(self):
        if self.gear == "N":
            print(f"Error: Car {self._name} is in gear N")
        else:
            self._speed += 1
            print(f"Car {self._name} is accelerating")


class CarWithTurbo(Car):
    def __init__(self, name: str):
        super().__init__(name)
        self._turbos = [2, 3]

    def accelerate(self, turbo: int):
        if self.gear == "N":
            print(f"Error: Car {self._name} is in gear N")
        elif turbo in self._turbos:
            self._speed += turbo
            print("Car %s is accelerating with turbo %d" % (self._name, turbo))


if __name__ == "__main__":
    # ## This works
    car = Car("Nissan Note")
    car.change_gear("1")
    car.accelerate()

    # ## But we can't replace Car with CarWithTurbo without breaking changes
    # ## If we do this, the program crashes
    autoCar = CarWithTurbo("Nissan GTR")
    autoCar.change_gear("1")
    autoCar.accelerate()

# %%


class CarInspector:
    def inspect(self, vehicle: Car):
        Car()
