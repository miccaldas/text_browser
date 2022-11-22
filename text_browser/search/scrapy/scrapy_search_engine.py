"""
We use scrapy to check Startpage first page of
results, for a given query. The results are clean
and shown to the user.
"""
import os
import subprocess

import click
import isort
import pyfiglet
import questionary
import snoop
from blessed import Terminal
from questionary import Style
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def search_engine():
    """
    Asks the user for a query, looks in
    the search engines for it and yanks
    ten results from each. Joins them
    in a enumerated list.
    """

    term = Terminal()

    with open("results.txt", "r") as f:
        lnk_lst = f.readlines()

    startpage_lnks = [i for i in lnk_lst if "startpage" in i]
    not_startpage = [i for i in lnk_lst if i not in startpage_lnks]
    eu_lnks = [i for i in not_startpage if i.startswith("https://eu-")]
    not_eu_lst = [i for i in not_startpage if i not in eu_lnks]
    not_ending = [i for i in not_eu_lst if i.endswith("=\n")]
    not_not_ending_lst = [i for i in not_eu_lst if i not in not_ending]
    slash_lst = [i for i in not_not_ending_lst if i.startswith("/")]
    not_slash_lst = [i for i in not_not_ending_lst if i not in slash_lst]
    stripped_lst = [i.strip() for i in not_slash_lst]
    clean_lst = list(set(stripped_lst))

    fig = pyfiglet.Figlet(font="larry3d")
    print(fig.renderText("search"))

    for item in clean_lst:
        print(item)

    custom_style_monitor = Style(
        [
            ("qmark", "fg:#8E806A bold"),
            ("question", "fg:#E0DDAA bold"),
            ("answer", "fg:#eeedde"),
            ("pointer", "fg:#BB6464 bold"),
            ("highlighted", "fg:#E5E3C9 bold"),
            ("selected", "fg:#94B49F bold"),
            ("separator", "fg:#ff5c8d"),
            ("instruction", "fg:#E4CDA7"),
            ("text", "fg:#F1E0AC bold"),
        ]
    )

    delete_shell_output = questionary.confirm(
        "Do you want to delete results.txt?",
        qmark="[X]",
        default="No",
        style=custom_style_monitor,
        auto_enter=False,
    ).ask()

    if delete_shell_output:
        os.remove("results.txt")


if __name__ == "__main__":
    search_engine()
