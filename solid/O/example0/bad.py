_ = """
Bad example not following OCP
https://levelup.gitconnected.com/s-o-l-i-d-principles-explained-in-python-with-examples-83b2b43bdcde

What is if we wanted to add "Super VIP" discount?
Is it possible to dot it without modifying existing code?
"""


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == "normal":
            return self.price * 0.1
        elif self.customer == "favorite":
            return self.price * 0.2
        elif self.customer == "vip":
            return self.price * 0.4
        else:
            raise NotImplementedError
