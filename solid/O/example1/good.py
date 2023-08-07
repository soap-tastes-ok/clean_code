#%%
"""Clean Code in Python - Chapter 4
The open/closed principle
Counter-example of the open/closed principle.
An example that does not comply with this principle and should be refactored.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Event(ABC):
    raw_data: dict

    @staticmethod
    @abstractmethod
    def meets_condition(event_data: dict) -> bool:
        return NotImplementedError


class UnknownEvent(Event):
    """A type of event that cannot be identified from its data."""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return False


class LoginEvent(Event):
    """A event representing a user that has just entered the system."""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return (event_data["before"]["session"] == 0) and (
            event_data["after"]["session"] == 1
        )


class LogoutEvent(Event):
    """An event representing a user that has just left the system."""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return (event_data["before"]["session"] == 1) and (
            event_data["after"]["session"] == 0
        )


class SystemMonitor:
    """Identify events that occurred in the system
    >>> l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
    >>> l1.identify_event().__class__.__name__
    'LoginEvent'
    >>> l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
    >>> l2.identify_event().__class__.__name__
    'LogoutEvent'
    >>> l3 = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
    >>> l3.identify_event().__class__.__name__
    'UnknownEvent'
    """

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        for e in Event.__subclasses__():
            if e.meets_condition(self.event_data):
                return e(self.event_data)
        return UnknownEvent(self.event_data)


data = [
    {"before": {"session": 0}, "after": {"session": 1}},  # Login
    {"before": {"session": 1}, "after": {"session": 0}},  # Logout
    {"before": {"session": 1}, "after": {"session": 1}},  # Unknown
]
for d in data:
    sm = SystemMonitor(d)
    print(sm.identify_event())

# %%
_ = """Add a Transaction event

>>> l4 = SystemMonitor({"before": {"session": 1},
>>> "after": {"session": 1, , "transaction": 1}})
>>> l4.identify_event().__class__.__name__
'TransactionEvent'
"""


class TransactionEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict) -> dict:
        if event_data["after"].get("transaction", None) is not None:
            return True


data = [
    {"before": {"session": 0}, "after": {"session": 1}},  # Login
    {"before": {"session": 1}, "after": {"session": 0}},  # Logout
    {"before": {"session": 1}, "after": {"session": 1}},  # Unknown
    {
        "before": {"session": 1},
        "after": {"session": 1, "transaction": 1},
    },  # transaction
]

for d in data:
    sm = SystemMonitor(d)
    print(sm.identify_event())
# %%
