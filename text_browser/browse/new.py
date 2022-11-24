"""Module Docstring"""
import pickle
import sys

import blessed
import requests
import snoop
from blessed import Terminal
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def new():
    """"""

    terminal = Terminal()
    term = blessed.Terminal()

    file = "https://docs.scrapy.org/en/latest/intro/tutorial.html"

    r = requests.get(file)

    print(type(r))
    pickle.dump(r, "r_zombie")


if __name__ == "__main__":
    new()
