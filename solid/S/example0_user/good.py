_ = """
Each class has one and only one responsibility.
"""


class User:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name


class UserDB:
    def load(self, id) -> User:
        # Code to load user data
        pass

    def save(self, user: User):
        # Code to save user data
        pass

