_ = """
GOOD example following OCP
https://levelup.gitconnected.com/s-o-l-i-d-principles-explained-in-python-with-examples-83b2b43bdcde
"""

#%%

from abc import ABC


class Discount(ABC):
    DISCOUNT_RATE: float = 0

    def __init__(self, price):
        self._price = price

    def give_discount(self):
        return self._price * self.DISCOUNT_RATE


class NormalDiscount(Discount):
    DISCOUNT_RATE = 0.1


class FavoriteDiscount(Discount):
    DISCOUNT_RATE = 0.2


class VipDiscount(Discount):
    DISCOUNT_RATE = 0.4


#%%

d = NormalDiscount(100)
print(f"Normal discount = {d.give_discount()}")

d = FavoriteDiscount(100)
print(f"Favorite discount = {d.give_discount()}")

d = VipDiscount(100)
print(f"VIP discount = {d.give_discount()}")

# %%
for D in Discount.__subclasses__():
    d = D(100)
    print(f"{D.__name__} = {d.give_discount()}")

# %%
d.__class__.__name__

# %%
