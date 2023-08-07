#%%
_ = """

"""

from abc import ABC, abstractmethod


class SuperClass(ABC):
    def common_method(self):
        """
        A concrete method can be defined/implemented
        inside an abstract class,
        if the method is common for all sub-classes.
        """
        print("I'm a common method for all sub-classes")
        # implement code ...

    @abstractmethod  # Forces implementation/override
    def uncommon_method(self):
        """
        @abstractmethod is used when a method
        is supposed to have different implementations
        in all sub-classes.
        Therefore, implementation of all
        abstract methods are forced in all sub-classes.
        """
        pass  # Just write "pass" for abstract methods
