#%%
_ = """
LSP: Better Example

Another solution is to separate "turbo" into its own method.
This way, replacing superclass with subclass won't throw error,
and also it's much less likely to introduce bug in main code.
"""


class Car:
    def __init__(self, name: str):
        self._name = name
        self._speed = 0
        self._accel = 1  # add 1 unit of speed
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
            self._speed += self._accel
            print(
                (
                    f"Car {self._name} is accelerating with {self._accel:+}"
                    + f" (Current speed is {self._speed:+})"
                )
            )


class CarWithTurbo(Car):
    def __init__(self, name: str):
        super().__init__(name)
        self._turbo = False

    def turbo_on(self):
        # Base case
        if self._turbo:
            print("Turbo is already ON")
            return
        self._accel += 1
        self._turbo = True
        print(f"Car {self._name} set turbo ON.")

    def turbo_off(self):
        # Base case
        if not self._turbo:
            print("Turbo is already OFF")
            return
        self._accel -= 1
        self._turbo = False
        print(f"Car {self._name} set turbo OFF.")


if __name__ == "__main__":
    # Assume "Car" is used in main code
    print("-" * 10 + "Original Code" + "-" * 10)
    car = Car("Nissan Note")
    car.change_gear("1")
    car.accelerate()

    # Replace "PassengerCar" with "CarWithTurbo"
    # --> No problem
    print("-" * 10 + "Replace super with sub class" + "-" * 10)
    turbo_car = CarWithTurbo("Nissan Note X")
    turbo_car.change_gear("1")
    turbo_car.accelerate()
    # This way it's much less likely to introduce bug in code
    print("-" * 10 + "Test" + "-" * 10)
    turbo_car = CarWithTurbo("Nissan Note X")
    turbo_car.change_gear("1")
    turbo_car.turbo_on()
    turbo_car.accelerate()
    turbo_car.accelerate()
    turbo_car.turbo_off()
    turbo_car.accelerate()


# %%
