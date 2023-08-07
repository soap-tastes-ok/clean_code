#%%

_ = """
You can do error catching
"""

from abc import ABC, abstractmethod


class KitchenAppliance(ABC):
    """Abstract class for kitchen appliances"""

    @abstractmethod  # Force implementation
    def on():
        raise NotImplementedError

    @abstractmethod  # Force implementation
    def off():
        raise NotImplementedError

    @abstractmethod  # Force implementation
    def set_temperature():
        raise NotImplementedError


class Toaster(KitchenAppliance):
    def on(self):
        # Some code to turn on Toaster
        pass

    def off(self):
        # Some code to turn off Toaster
        pass

    def set_temperature(self):
        # Some code to set temperature of Toaster
        pass


class Juicer(KitchenAppliance):
    def on(self):
        # Some code to turn on Juicer
        pass

    def off(self):
        # Some code to turn off Juicer
        pass


if __name__ == "__main__":
    # Throws error
    juicer = Juicer()
    # Below throws error too
    Juicer.set_temperature()

# %%
