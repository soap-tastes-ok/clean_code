#%%
_ = """
LSP: Better Example

Another solution is to make the interface of "Car" and "CarWithTurbo" the same.

This also doesn't cause error, but can still cause bug.

1. If you forget to update "add_speed" value,
    your CarWithTurbo won't accelerate with turbo.
2. You can also technically set your "Car" to turbo
    bypassing large number to "Car.accelerate()" method.
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

    def accelerate(self, add_speed: int):
        if self._gear == "N":
            print(f"Error: Car {self._name} is in gear N")
        else:
            self._speed += add_speed
            print(f"Car {self._name} is accelerating with {add_speed:+}")


class CarWithTurbo(Car):
    def __init__(self, name: str):
        super().__init__(name)

    def accelerate(self, add_speed: int):  # Make interface same
        if self._gear == "N":
            print(f"Error: Car {self._name} is in gear N")
        else:
            self._speed += add_speed
            print(f"Car {self._name} is accelerating with {add_speed:+}")


if __name__ == "__main__":
    # Assume "Car" is used in main code
    car = Car("Nissan Note")
    car.change_gear("1")
    car.accelerate(1)

    # If we replace "Car" with "CarWithTurbo"
    # --> Doesn't cause error but can still cause bug
    turbo_car = CarWithTurbo("Nissan Note X")
    turbo_car.change_gear("1")
    turbo_car.accelerate(1)

# %%
