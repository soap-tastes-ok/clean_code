#%%
_ = """
LSP: Better Example

One solution is to add default parameter
to "turbo" argument in CarWithTurbo.accelerate() method.

This doesn't cause error, but can still cause bug.
What is if your turbo parameter is not a fixed value?
"""


class Car:
    def __init__(self, name: str):
        self._name = name
        self._speed = 0
        self._gears = ["N", "1", "2", "3", "4", "5", "6"]
        self._gear = "N"

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

    def accelerate(self, turbo: int = 1):  # ⭐️ Add default param
        if self.gear == "N":
            print(f"Error: Car {self._name} is in gear N")
        else:
            self._speed += 1 + turbo
            print(f"Car {self._name} is accelerating with {1 + turbo:+}")


if __name__ == "__main__":
    # Assume "Car" is used in main code
    car = Car("Nissan Note")
    car.change_gear("1")
    car.accelerate()

    # If we replace "Car" with "CarWithTurbo"
    # --> Doesn't cause error, but can still cause bug
    turbo_car = CarWithTurbo("Nissan Note X")
    turbo_car.change_gear("1")
    turbo_car.accelerate()

# %%
