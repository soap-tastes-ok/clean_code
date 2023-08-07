#%%
class KitchenAppliance:
    """Super-class"""

    def on(self):
        pass

    def off(self):
        pass


class KitchenApplianceWithTemp(KitchenAppliance):
    """Extended super-class"""

    def set_temperature(self):
        pass


class Toaster(KitchenApplianceWithTemp):
    """Sub-class 1"""

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
    """Sub-class 2"""

    def on(self):
        # Some code to turn on Toaster
        pass

    def off(self):
        # Some code to turn off Toaster
        pass


if __name__ == "__main__":
    # ## Assume both super-classes are being used in main code
    # ...
    kitchen_app = KitchenAppliance()
    kitchen_app.on()
    kitchen_app.off()
    # ...
    kitchen_app_temp = KitchenApplianceWithTemp()
    kitchen_app_temp.on()
    kitchen_app_temp.set_temperature()
    kitchen_app_temp.off()
    # ...

    # Replace both super-classes with their sub-classes
    # ...
    juicer = Juicer()
    juicer.on()
    juicer.off()
    # ...
    toaster = Toaster()
    toaster.on()
    toaster.set_temperature()
    toaster.off()
    # ...
    # --> This will throw no error!

# %%
