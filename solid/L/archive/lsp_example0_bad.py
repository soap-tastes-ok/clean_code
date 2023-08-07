#%%

from abc import ABC, abstractmethod


class Sender(ABC):
    @abstractmethod
    def send(self, message):
        pass


class Email(Sender):
    def send(self, message: str, email: str):
        print(f"Send '{message}' to {email}")


class SMS(Sender):
    def send(self, message: str, phone: int):
        print(f"Send '{message}' to {phone}")


if __name__ == "__main__":
    notification = Email()  # Can we replace Email with SMS
    notification.send("Hello", "john@test.com")

# %%
