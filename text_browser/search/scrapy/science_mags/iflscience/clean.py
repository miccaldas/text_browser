"""
Cleans output of Scrapy spider.
"""
import json
import re

import snoop
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def clean():
    """
    We erase the first entries in text, as they are not
    content. As the text is in list form, it's needed
    to transform it ro string, so as to be able to read
    it as one. The author field was a list that repeated
    the author's name twice. Adding a line break after a
    punctuation mark is needed ease the reading effort.
    """
    with open("items1.json") as f:
        data = json.load(f)

    entry_lst = []
    for i in data:
        i["text"] = i["text"][10:-6]
        i["text"] = "".join(i["text"])
        if i["author"] != []:
            i["author"] = i["author"][0]
        i["text"] = re.sub("\.", ".\\n", i["text"])

    for i in data:
        with open(f'{i["title"]}.txt', "w") as f:
            f.write(f"{i['text']}")

    for d in data:
        print(d)


if __name__ == "__main__":
    clean()
