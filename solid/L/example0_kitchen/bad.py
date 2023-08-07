class KitchenAppliance:
    def on(self):
        # Some code to turn on
        print("Turning ON 'KitchenAppliance'")

    def off(self):
        # Some code to turn off
        print("Turning OFF 'KitchenAppliance'")

    def set_temperature(self):
        # Some code to set temperature
        print("Setting temp for 'KitchenAppliance'")


class Toaster(KitchenAppliance):
    def on(self):
        # Some code to turn on Toaster
        print("Turning ON 'Toaster'")

    def off(self):
        # Some code to turn off Toaster
        print("Turning OFF 'Toaster'")

    def set_temperature(self):
        # Some code to set temperature of Toaster
        print("Setting temp for 'Toaster'")


class Juicer(KitchenAppliance):
    def on(self):
        # Some code to turn on Juicer
        print("Turning ON 'Juicer'")

    def off(self):
        # Some code to turn off Juicer
        print("Turning OFF 'Juicer'")


if __name__ == "__main__":
    print("-" * 10 + "original code" + "-" * 10)
    # Assume super-class is being used in main code
    kitchen_app = KitchenAppliance()
    kitchen_app.on()
    kitchen_app.set_temperature()
    kitchen_app.off()
    print("-" * 10 + "Test LSP 1" + "-" * 10)
    # Replace super class with Toaster sub class
    # --> No problem
    toaster = Toaster()
    toaster.on()
    toaster.set_temperature()
    toaster.off()
    print("-" * 10 + "Test LSP 2" + "-" * 10)
    # Replace super class with Juicer sub class
    # --> Can cause unexpected behavior!
    juicer = Juicer()
    juicer.on()
    juicer.set_temperature()  # What will this do..?
    juicer.off()
