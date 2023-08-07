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

    @property
    def create(self):
        return _PointFactory()


class _PointFactory:
    """Factory class for "wholesale" creation of Point class"""

    def from_cartesian(self, x, y):
        return Point(x, y)

    def from_polar(self, rho, theta):
        x = rho * math.cos(theta)
        y = rho * math.sin(theta)
        return Point(x, y)


p = Point()
p1 = p.create.from_cartesian(2, 3)
p2 = p.create.from_polar(1, math.pi / 4)
print(p1)
print(p2)

# %%
