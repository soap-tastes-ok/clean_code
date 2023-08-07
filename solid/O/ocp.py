_ = """
Specification pattern
"""


#%%
import enum
from abc import ABC, abstractmethod
from enum import Enum, Flag


#### Objects
class Size(Enum):
    SMALL = enum.auto()
    MEDIUM = enum.auto()
    LARGE = enum.auto()


class Color(Flag):
    BLUE = enum.auto()  # 1 = 0b001
    GREEN = enum.auto()  # 2 = 0b010
    RED = enum.auto()  # 4 = 0b100
    CYAN = GREEN | BLUE  # 0b010 | 0b001 = 0b11 = 3
    MAGENTA = RED | BLUE  # 0b100 | 0b001 = 0b101 = 5
    YELLOW = RED | GREEN  # 0b100 | 0b010 = 0b110 = 6
    WHITE = RED | GREEN | BLUE  # 0b100 | 0b010 | 0b001 = 0b111 = 7
    BLACK = RED & GREEN & BLUE  # 0b100 & 0b010 & 0b001 = 0b000 = 0
    AQUA = CYAN
    FUCHSIA = MAGENTA


class Product:
    def __init__(self, name: str, color: str, size: int):
        self._name = name
        self._color = color
        self._size = size

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    @property
    def size(self):
        return self._size


### Specification pattern

# Abstract base classes


class Specification(ABC):
    @abstractmethod
    def is_satisfied(self, item):
        raise NotImplementedError

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)


class Filter(ABC):
    @abstractmethod
    def filter(self, items, spec):
        raise NotImplementedError


# Concrete classes


class AndSpecification(Specification):
    """Combinator"""

    def __init__(self, *args) -> None:
        self._args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self._args))


class OrSpecification(Specification):
    """Combinator"""

    def __init__(self, *args) -> None:
        self._args = args

    def is_satisfied(self, item):
        return any(map(lambda spec: spec.is_satisfied(item), self._args))


class SizeSpecification(Specification):
    def __init__(self, size: Size) -> None:
        self._size = size

    def is_satisfied(self, item):
        return item.size == self._size


class ColorSpecification(Specification):
    def __init__(self, color: Color) -> None:
        self._color = color

    def is_satisfied(self, item):
        return item.color == self._color


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    # Specifications
    red = ColorSpecification(Color.RED)
    blue = ColorSpecification(Color.BLUE)
    green = ColorSpecification(Color.GREEN)
    large = SizeSpecification(Size.LARGE)
    small = SizeSpecification(Size.SMALL)
    large_green = green & large
    large_or_small = large | small
    blue_or_red = blue | red

    # Filter
    bf = BetterFilter()
    for p in bf.filter(products, large_or_small):
        print(p.name)

    # for p in products:
    #     if large_or_small.is_satisfied(p):
    #         print(p.name)


# %%
