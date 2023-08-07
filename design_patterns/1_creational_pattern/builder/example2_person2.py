# %%
class Class:
    INDENT_SIZE = 2

    def __init__(self, class_name):
        self._class_name = class_name
        self.attributes = []

    def _code_formatter(self):
        formated_code = [f"class {self._class_name}:"]
        indent_1 = " " * self.INDENT_SIZE * 1
        if len(self.attributes) == 0:
            formated_code.append("{}pass".format(indent_1))
        else:
            formated_code.append("{}def __init__(self):".format(indent_1))
            indent_2 = " " * self.INDENT_SIZE * 2
            for key, value in self.attributes:
                formated_code.append("{}self.{} = {}".format(indent_2, key, value))
        return "\n".join(formated_code)

    def __str__(self):
        return self._code_formatter()


class CodeBuilder:
    def __init__(self, class_name):
        self._class_name = class_name
        self._class = Class(class_name)

    def add_field(self, key, value):
        self._class.attributes.append((key, value))
        return self

    def __str__(self):
        return str(self._class)


cb = CodeBuilder("Person")
cb.add_field("name", '""').add_field("age", "0")
print(cb)

# %%
bool([])
# %%
