"""
Module where we clean the output of the json file,
and create a text file with all the information
per page.
"""
import json
import re

import snoop
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def clean_results():
    """
    We first convert the json file to a dictionary,
    then we create a list to house the results per
    page. In order to preserve the line breaks of
    the original, we need to add to all points a
    line break symbol.
    We then do some manipulations to the title, in
    order to create a good file title and create a
    text file per page.
    """
    with open("results.json") as f:
        data = json.load(f)

    breaks = []
    no_spaces_line_breaks = []
    for i in data:
        breaks.append(f'{i["title"]}\n')
        breaks.append(i["author"])
        for d in i["text"]:
            brk = re.sub("\.", ".\\n", d)
            breaks.append(brk)
        no_spaces_line_breaks.append(breaks)
        space = i["title"].replace(" ", "_")
        tit = space.lower()
        with open(f"{tit}.txt", "w") as f:
            for line in no_spaces_line_breaks:
                for il in line:
                    f.write(il)


if __name__ == "__main__":
    clean_results()
