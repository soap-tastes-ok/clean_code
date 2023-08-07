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
class HTMLElement:
    INDENT_SIZE = 4

    def __init__(self, name, text="") -> None:
        self._name = name
        self._text = text
        self.elements = []

    def __str_helper(self, n_indent=0):
        lines = []
        i = " " * self.INDENT_SIZE * n_indent
        lines.append(f"{i}<{self._name}>")
        if self._text:
            i1 = " " * self.INDENT_SIZE * (n_indent + 1)
            lines.append(f"{i1}{self._text}")

        for e in self.elements:
            _sub_str = e.__str_helper(n_indent + 1)
            lines.append(_sub_str)
        lines.append(f"{i}</{self._name}>")
        return "\n".join(lines)

    def __str__(self) -> str:
        return self.__str_helper()

    @staticmethod
    def create(name):
        return HTMLBuilder(name)


class HTMLBuilder:
    def __init__(self, root_name: str) -> None:
        self._root_name = root_name
        self._root = HTMLElement(root_name, "Yoyoyo")

    def add_child(self, name: str, text: str):
        self._root.elements.append(HTMLElement(name, text))
        return self

    def __str__(self) -> str:
        return str(self._root)


# %%
if __name__ == "__main__":
    builder = HTMLBuilder("ul")
    builder.add_child("li", "Haha I'm a child")
    builder.add_child("li", "Yoyo I'm child #2")
    builder._root.elements[0].elements.append(HTMLElement("li", "Yoyo I'm grand-child"))
    print(builder)


# %%
if __name__ == "__main__":
    builder = HTMLElement.create("ul")
    builder.add_child("li", "Haha I'm a child")
    builder.add_child("li", "Yoyo I'm child #2")
    builder._root.elements[0].elements.append(HTMLElement("li", "Yoyo I'm grand-child"))
    print(builder)

# %%
