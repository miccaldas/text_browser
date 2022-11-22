"""Module Docstring"""
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger

from scrapy_project_class import ScrapyProject


@logger.catch
@snoop
def main():
    """"""

    with open("/usr/share/nginx/html/feeds/support_files/rss_text/Mercury-SB4_comparison/sample/apagar", "r") as f:
        lines = f.readlines()
        newlines = []
        for line in lines:
            newlines.append(line.rstrip())

    link_keys = [
        "entry1",
        "entry2",
        "entry3",
        "entry4",
        "entry5",
        "entry6",
        "entry7",
        "entry8",
        "entry9",
        "entry10",
        "entry11",
        "entry12",
        "entry13",
        "entry14",
        "entry15",
        "entry16",
        "entry17",
        "entry18",
        "entry19",
        "entry20",
    ]

    spider_names = ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10", "e11", "e12", "e13", "e14", "e15", "e16", "e17", "e18", "e19", "e20"]

    proj_attr = zip(link_keys, spider_names)
    pro_att = []
    for bi in proj_attr:
        pro_att.append(bi)

    conditions = []
    for i in range(len(newlines)):
        conditions.append(pro_att[i] + (newlines[i],))

    for condition in conditions:
        scrapyproj = ScrapyProject(condition[0], condition[1], condition[2])
        scrapyproj.project_creation()
        scrapyproj.settings_definition()
        scrapyproj.spider()


if __name__ == "__main__":
    main()
