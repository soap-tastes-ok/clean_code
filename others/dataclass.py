#%%

from dataclasses import dataclass, field


@dataclass(frozen=False)
class Person:
    sort_index: int = field(init=False, repr=False)
    age: int
    sex: str
    height: int = field(default=None, init=True, repr=True, compare=False)
    weight: int = field(
        default=None,
        init=True,
        repr=True,
        compare=False,
    )

    def __post_init__(self):
        self.sort_index = self.age


max = Person(15, "male", height=180)
brian = Person(15, "male", height=190)

max == brian

# %%
