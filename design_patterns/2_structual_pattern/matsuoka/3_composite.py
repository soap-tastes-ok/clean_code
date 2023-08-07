import abc
import sys


def main():
    ruler = SimpleItem("Ruler", 1.60)
    eraser = SimpleItem("Eraser", 0.20)
    pencil = SimpleItem("Pencil", 0.40)
    pencilset = CompositeItem("Pencil Set", pencil, eraser, ruler)

    box = SimpleItem("Box", 1.00)
    boxedpencilset = CompositeItem("Boxed Pencil Set", box, pencilset)
    boxedpencilset.add(pencil)

    for item in [pencil, ruler, eraser, pencilset, boxedpencilset]:
        item.print()


# Component
class AbstractItem(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def composite(self):
        pass

    def __iter__(self):
        return iter([])


# Leaf
class SimpleItem(AbstractItem):
    def __init__(self, name, price=0.00):
        self.name = name
        self.price = price

    def print(self, indent="", file=sys.stdout):
        print("{}${:.2f} {}".format(indent, self.price, self.name), file=file)

    @property
    def composite(self):
        return False


# Composite
class AbstractCompositeItem(AbstractItem):
    def __init__(self, *items):
        self.children = []
        if items:
            self.add(*items)

    def add(self, first, *items):
        self.children.append(first)
        if items:
            self.children.extend(items)

    def remove(self, item):
        self.children.remove(item)

    def __iter__(self):
        return iter(self.children)


# (Composite)
class CompositeItem(AbstractCompositeItem):
    def __init__(self, name, *items):
        super().__init__(*items)
        self.name = name

    def print(self, indent="", file=sys.stdout):
        print("{}${:.2f} {}".format(indent, self.price, self.name))
        for child in self:
            child.print(indent + " ")

    @property
    def composite(self):
        return True

    @property
    def price(self):
        return sum(item.price for item in self)


if __name__ == "__main__":
    main()
