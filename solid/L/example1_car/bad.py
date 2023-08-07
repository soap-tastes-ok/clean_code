#%%
_ = """
LSP: Bad Example

Against LSP.
Replacing super-class (i.e. Car) with sub-class (i.e. CarWithTurbo)
causes error.
"""


class Car:
    def __init__(self, name: str):
        self._name = name
        self._speed = 0
        self._gears = ["N", "1", "2", "3", "4", "5", "6"]
        self._gear = "N"

    def change_gear(self, gear: str):
        if gear in self._gears:
            self._gear = gear
            print(f"Car {self._name} is in gear {self._gear}")

    def accelerate(self):
        if self._gear == "N":
            print(f"Error: Car {self._name} is in gear N")
        else:
            self._speed += 1
            print(f"Car {self._name} is accelerating")


class CarWithTurbo(Car):
    def __init__(self, name: str):
        super().__init__(name)

    def accelerate(self, turbo: int):
        if self._gear == "N":
            print(f"Error: Car {self._name} is in gear N")
        else:
            self._speed += 1 + turbo
            print("Car %s is accelerating with turbo %d" % (self._name, turbo))


if __name__ == "__main__":
    note = Car("Nissan Note")
    note.change_gear("1")
    note.accelerate()

    # Now replace "Car" with its sub-class "CarWithTurbo"
    gtr = CarWithTurbo("Nissan GTR")
    note.change_gear("1")
    gtr.accelerate()  # This raises Error (brakes LSP)

#%%

_ = """

So why is braking LSP a problem?

Ok, let's say we have another class
that does 車検 for all cars.
This breaks too, so every time
we have a new Car type,
we have to add an "if else condition"
in the "CarInspector.inspect" class...!!!!
"""


class CarInspector:
    def inspect(self, car: Car):
        print("-" * 10 + "Start inspection" + "-" * 10)
        for gear in car._gears:
            car.change_gear(gear)
            car.accelerate()


if __name__ == "__main__":
    note = Car("Nissan Note")
    gtr = CarWithTurbo("Nissan GTR")

    inspector = CarInspector()
    inspector.inspect(note)
    inspector.inspect(gtr)

# %%
