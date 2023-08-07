# %%
from abc import ABC, abstractmethod
from enum import Enum, auto


# Drinks
class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This tea is nice but I'd prefer it with milk")


class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicious")


# Make Enum class
all_drinks = [c.__name__ for c in HotDrink.__subclasses__()]
AvailableDrinks = Enum("AvailableDrinks", all_drinks)


# Drink factories
class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Put in tea bag, boil water, pour {amount}ml, enjoy!")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Grind some beans, boil water, pour {amount}ml, enjoy!")
        return Coffee()


class HotDrinkMachine:
    FACTORIES = []
    INITIALIZED = False

    def __init__(self):
        if self.INITIALIZED:
            return
        for d in AvailableDrinks:
            factory_name = f"{d.name}Factory"
            factory_instance = eval(factory_name)()
            self.FACTORIES.append((d.name, factory_instance))
        self.INITIALIZED = True

    def make_drink(self):
        print("Available drinks:")
        for i, d in enumerate(self.FACTORIES):
            print(f"{i}: {d[0]}")
        import time

        time.sleep(0.1)

        s = input(f"Please pick drink (0-{len(self.FACTORIES)-1}): ")
        idx = int(s)
        s = input("Specify amount: ")
        amount = int(s)
        return self.FACTORIES[idx][1].prepare(amount)


if __name__ == "__main__":
    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()
