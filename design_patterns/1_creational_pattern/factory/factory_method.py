# %%

import enum
from enum import Enum
import math


class CoordinateSystem(Enum):
    CARTESIAN = enum.auto()
    POLAR = enum.auto()


class Point:
    def __init__(self, x=None, y=None) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return str(f"{self.x = }, {self.y = }")

    @staticmethod
    def from_cartesian(x, y):
        """Factory Method for "wholesale" creation of Point class"""
        return Point(x, y)

    @staticmethod
    def from_polar(rho, theta):
        """Factory Method for "wholesale" creation of Point class"""
        x = rho * math.cos(theta)
        y = rho * math.sin(theta)
        return Point(x, y)


p = Point()
p1 = p.from_cartesian(2, 3)
p2 = p.from_polar(1, math.pi / 4)
print(p1)
print(p2)

# %%
