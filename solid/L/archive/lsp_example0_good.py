#%%

from abc import ABC, abstractmethod


class Sender(ABC):
    @abstractmethod
    def send(self, message):
        pass


class Email(Sender):
    def __init__(self, email):
        self._email = email

    def send(self, message):
        print(f"Send '{message}' to {self._email}")


class SMS(Sender):
    def __init__(self, phone):
        self._phone = phone

    def send(self, message):
        print(f"Send '{message}' to {self._phone}")


if __name__ == "__main__":
    notification = Email("john@test.com")
    notification.send("Hello")


# %%
