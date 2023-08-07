"""
Creational - Builder design pattern

Purpose:
Split API when you have complex construction of object
(i.e. many steps in initialization).

Example:
Making a house. How many windows? Need a chimney?
Need a garage? How many rooms? Need a garden? Etc etc etc

Example 2:
Defining and making HTML from scratch.
"""


# %%
class Person:
    def __init__(self):
        print("Creating an instance of Person")
        # address
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment info
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return (
            f"Address: {self.street_address}, {self.postcode}, {self.city}\n"
            + f"Employed at {self.company_name} as a {self.position} earning {self.annual_income}"
        )

    @staticmethod
    def create():
        return _PersonBuilder()


class _PersonBuilder:
    def __init__(self, person=Person()) -> None:
        self._person = person

    def __str__(self) -> str:
        return str(self._person)

    @property
    def works(self):
        return _PersonJobBuilder(self._person)

    @property
    def lives(self):
        return _PersonAddressBuilder(self._person)


class _PersonJobBuilder(_PersonBuilder):
    def __init__(self, person: Person) -> None:
        super().__init__(person)

    def at(self, company_name: str):
        self._person.company_name = company_name
        return self

    def as_a(self, position: str):
        self._person.position = position
        return self

    def earning(self, annual_income: int):
        self._person.annual_income = annual_income
        return self


class _PersonAddressBuilder(_PersonBuilder):
    def __init__(self, person: Person) -> None:
        super().__init__(person)

    def at(self, street_address):
        self._person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self._person.postcode = postcode
        return self

    def in_city(self, city):
        self._person.city = city
        return self


if __name__ == "__main__":
    person = Person.create()
    person.works.at("SoftBank Group Corp.").as_a("Engineer").earning("100Yen")
    # .lives.at("")
    print(person)

# %%
