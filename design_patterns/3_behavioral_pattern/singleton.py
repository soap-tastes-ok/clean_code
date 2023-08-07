#%%


class A:
    def test(self):
        print("A")


class B(A):
    def test(self):
        print("B")
        A().test()


class C(A):
    def test(self):
        print("C")
        A().test()


class D(B, C):
    def test(self):
        print("D")
        B().test()
        C().test()


d = D()

d.test()

# %%
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class FactoryConfig(metaclass=SingletonMeta):
    def __init__(self, log_level="INFO"):
        self.log_level = log_level

    @classmethod
    def reset(cls):
        cls._instances = {}


class A(FactoryConfig):
    def __init__(self, log_level="INFO"):
        super().__init__(log_level)


class Factory_A:
    def __init__(self, config):
        self.config = config

    def show_config(self):
        return self.config


class Factory_B:
    def __init__(self, config):
        self.config = config

    def show_config(self):
        return self.config


def main():
    config = A(log_level="DEBUG")
    factory_a = Factory_A(config)
    print(factory_a.__class__.__name__)
    print(vars(factory_a.show_config()))

    A.reset()
    bad_config = A(log_level="WARNING")
    factory_b = Factory_B(bad_config)
    print(factory_b.__class__.__name__)
    print(vars(factory_a.show_config()))


if __name__ == "__main__":
    main()

# %%
