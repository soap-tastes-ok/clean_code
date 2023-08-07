import abc
import sys


def main():
    title = "Monthly Report"
    texts = ["good", "best"]

    pr = PlainTextReporter()
    pr.header(title)
    pr.main(texts)
    pr.footer()

    print("\n\n")

    hr = HtmlReporterInheritance()
    # or
    # hr = HtmlReporterDelegation()
    hr.header(title)
    hr.main(texts)
    hr.footer()


# Adaptee
class HtmlWriter:
    def __init__(self, file=sys.stdout):
        self.file = file

    # oldMethod
    def out_header(self):
        self.file.write("<!doctype html>\n<html>\n")

    # oldMethod
    def out_title(self, title):
        self.file.write("<head><title>{}</title></head>\n".format(title))

    # oldMethod
    def out_start_body(self):
        self.file.write("<body>\n")

    # oldMethod
    def out_body(self, texts):
        for text in texts:
            self.file.write("<p>{}</p>\n".format(text))

    # oldMethod
    def out_end_body(self):
        self.file.write("</body>\n")

    # oldMethod
    def out_footer(self):
        self.file.write("</html>\n")


# Target
class Reporter(metaclass=abc.ABCMeta):
    # requiredMethod()
    @abc.abstractmethod
    def header(self, title):
        pass

    # requiredMethod()
    @abc.abstractmethod
    def main(self, contents):
        pass

    # requiredMethod()
    @abc.abstractmethod
    def footer(self):
        pass


class PlainTextReporter(Reporter):
    def __init__(self, file=sys.stdout):
        self.file = file

    # requiredMethod()
    def header(self, title):
        self.file.write("**{}**\n".format(title))

    # requiredMethod()
    def main(self, texts):
        for text in texts:
            self.file.write("{}\n".format(text))

    # requiredMethod()
    def footer(self):
        pass


# Adapter 継承Ver
class HtmlReporterInheritance(Reporter, HtmlWriter):
    def __init__(self, file=sys.stdout):
        self.file = file

    # requiredMethod()
    def header(self, title):
        self.out_header()
        self.out_title(title)
        self.out_start_body()

    # requiredMethod()
    def main(self, texts):
        self.out_body(texts)

    # requiredMethod()
    def footer(self):
        self.out_end_body()
        self.out_footer()


# Adapter 委譲Ver
class HtmlReporterDelegation(Reporter):
    def __init__(self, file=sys.stdout):
        self._htmlwriter = HtmlWriter(file)

    # requiredMethod()
    def header(self, title):
        self._htmlwriter.out_header()
        self._htmlwriter.out_title(title)
        self._htmlwriter.out_start_body()

    # requiredMethod()
    def main(self, texts):
        self._htmlwriter.out_body(texts)

    # requiredMethod()
    def footer(self):
        self._htmlwriter.out_end_body()
        self._htmlwriter.out_footer()


if __name__ == "__main__":
    main()
