#%%
_ = """
Below is code without using abc module.
"""


class Animal:
    def eat(self):
        pass

    def move(self):
        pass


class Dog(Animal):
    def eat(self):
        print("Dog: Chomp chomp")

    def move(self):
        print("Dog: Walk walk")


class Snake(Animal):
    def hiss(self):
        print("Snake: Ssssssssssss")


if __name__ == "__main__":
    # Snake should throw an error!
    snake = Snake()
    snake.move()
    # Shouldn't be able to call a base class!
    animal = Animal()
    animal.move()


#%%
_ = """
Below is code using abc module.
"""

from abc import ABC, abstractmethod


class Animal(ABC):  # Tells everyone this is an abstract class
    @abstractmethod  # Forces implementation/override
    def eat(self):
        pass

    @abstractmethod  # Forces implementation/override
    def move(self):
        pass


class Snake(Animal):
    def hiss(self):
        print("Snake: Ssssssssssss")


#%%
if __name__ == "__main__":
    # Snake now throws error
    snake = Snake()

# %%
if __name__ == "__main__":
    # Calling Animal class is now prohibited
    animal = Animal()

# %%
