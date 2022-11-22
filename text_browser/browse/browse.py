"""Module Docstring"""
import subprocess
import sys

import html2text
import isort
import pyfiglet
import requests
import snoop
from blessed import Terminal
from snoop import pp

from text_browser.search import search_engine


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def get_request():
    """"""

    url = search_engine.search_engine()

    r = requests.get(url)
    content = r.text

    def content_file():
        """"""
        cont = html2text.html2text(content)
        with open("content.txt", "w") as f:
            f.write(cont)
        cmd = "rich 'content.txt' --pager --theme nord"
        subprocess.run(cmd, shell=True)

    if len(content) == 0:
        if r.status_code == 200:
            content_file()
        elif r.status_code == 400:
            print("Error 404, Not Found")
        elif r.status_code == 500:
            print("Error 500, Internal server error")
        else:
            content_file()
    else:
        content_file()

    return content


if __name__ == "__main__":
    get_request()


@snoop
def main():
    """"""

    fig = pyfiglet.Figlet(font="larry3d")
    print(fig.renderText("browser"))

    while True:
        link = input("URL: ")
        if link == "quit":
            break
        get_request(link)


if __name__ == "__main__":
    main()
