#%%
##############################
# Exampe 1: Class properties #
##############################


class Example1:
    def __init__(self):
        """Class の getter と setter の例

        基本的に __init__ 内の変数は全て
        変数名の頭に "_" や "__" をつけて
        デフォルトで外から全てアクセスできないようにする。
        "_" と "__" はどちらでもいいが、
        "_" は「触らないでね」という意味でしかなく
        実際はアクセスできるのに対して、
        "__" はより強めにアクセス制限をかけて
        AttributeErrorを吐くようにする。
        長いコードのどこかで間違って変数を上書きしたりして
        バグが起きなようにする為のルール。

        その中から、外から read できるようにしたい
        変数を "@property" decortor を使って
        class property として定義してあげて、
        外から write できるようにしたい変数を
        "@{変数名}.setter" decortor を使って
        setter を定義してあげる。


        """
        # 外から read も write もできない
        self.__private = 111
        # 外から read だけできる（ように設定したい変数）
        self.__only_read = 222
        # 外から read も write もできる（ように設定したい変数）
        self.__read_write = 333

    @property
    def only_read(self):
        """self.__only_read のread権限
        ユーザーは Example.only_read で値を呼び出せる
            >>> print(Example.only_read)
            222
        """
        return self.__only_read

    @property
    def read_write(self):
        """self.__read_writeのread権限
        ユーザーは Example.read_write で値を呼び出せる
            >>> print(Example.read_write)
            333
        """
        return self.__read_write

    @read_write.setter
    def read_write(self, read_write):
        """self.__read_write へのwrite権限
        ユーザーは Example.read_write = 999
        のように値を上書きできる
            >>> Example.read_write = 999
            >>> print(Example.read_write)
            999
        """
        self.__read_write = read_write


# %%
###### E1AMPLE 1
E1 = Example1()

# %%
# 外から read できる
E1.only_read

#%%
# 外から write できない
E1.only_read = 999

# %%
# 外から read できる
E1.read_write

#%%
# 外から write もできる
E1.read_write = 999

#%%
# 外から read できない
print(E1.__private)

#%%
# 頑張れば外から read できる。
# ので、Javaのような多言語と違って
# 完璧な private method ではない。
print(E1._Example1__private)

#%%
# 上書きはできちゃう。
E1.__private = "TEST"

# "_" や "__" がついている変数は
# 基本「触るな」という意味なので
# クラスの外からは触らないのがルール。


# %%
# 存在しない変数を外から新しく定義できちゃう。
E1.awdawddadaw = 999

# "E1.__private = 'TEST'" も
# 新しい変数が作られて上書きされてる。


# %%
###########################
# Exampe 2: Class methods #
###########################


class Example2:
    """Class の private/public method の例"""

    def public_function(self):
        """Can be accessed from outside"""
        self.__print()

    def _fake_private_function(self):
        """Has one "_", which means don't touch it
        but still can be accessed from outside.
        """
        self.__print()

    def __private_function2(self):
        """Has two "_", which means
        it can NOT be accessed from outside.
        """
        self.__print()

    def __print(self):
        """Just for utility so ignore this method"""
        print("Succesfully called method")


E2 = Example2()

#%%
E2.public_function()

#%%
E2._fake_private_function()

#%%
E2.__private_function2()


#%%

###########################################################
# Example 3: Prevent dynamic creation of class properties #
###########################################################

from functools import wraps


def freeze_class(cls):
    """Class decorator to prevent dynamic creation of properties

    ### Normal class behavior ###

    class NormalClass:
        def __init__(self):
            self.bar = 10

    foo = NormalClass()
    foo.bar = 42
    foo.foobar = "no way (T_T)"  # Doesn't raise Error 🥲
    print(foo.foobar)

    >> "no way (T_T)"

    ### With this decorator ###

    @freeze_class
    class Foo:
        def __init__(self):
            self.bar = 10

    foo = Foo()
    foo.bar = 42
    foo.foobar = "no way (T_T)" # Raises Error!

    >>> Class Foo is frozen. Cannot set foobar = no way

    Reference:
        https://stackoverflow.com/a/29368642
    """
    cls.__frozen = False

    def frozensetattr(self, key, value):
        if self.__frozen and not hasattr(self, key):
            print(
                f"Class {cls.__name__} is frozen."
                + f" Cannot set {key} = {value}"
            )
        else:
            object.__setattr__(self, key, value)

    def init_decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            self.__frozen = True

        return wrapper

    cls.__setattr__ = frozensetattr
    cls.__init__ = init_decorator(cls.__init__)

    return cls


#%%
class NormalClass:
    def __init__(self):
        self.bar = 10


foo = NormalClass()
foo.bar = 42
foo.foobar = "no way"  # Doesn't raise Error 🥲
print(foo.foobar)


#%%
@freeze_class
class FrozenClass:
    def __init__(self):
        self.bar = 10


foo = FrozenClass()
foo.bar = 42
foo.foobar = "no way"  # Raises Error!


#%%
