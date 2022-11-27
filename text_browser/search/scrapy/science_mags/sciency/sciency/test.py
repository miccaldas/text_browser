"""Module Docstring"""
import scrapy
import snoop
from items import SciencyItem
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def test():
    """"""
    it = SciencyItem()
    print(it["title"])


if __name__ == "__main__":
    test()
