_ = """
Below is Given a class which violates
the Single Responsibility Principle.
"""


class User:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def save(self, user):
        # Some code that saves user info
        pass

