"""
Searches, in Startpage, Bing and Google,
for a query made by the user.
"""
import re
import sys

import pyfiglet
import questionary
import snoop
from blessed import Terminal
from questionary import Style
from ScrapeSearchEngine.ScrapeSearchEngine import Bing, Google, Startpage
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
    in a enumerated list. This module can
    be imported and ran in 'browse.py'.
    """

    term = Terminal()

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

    userAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    srch_query = questionary.text("What are you looking for?", qmark="[X]", style=custom_style_monitor).ask()

    startpage = Startpage(srch_query, userAgent)
    google = Google(srch_query, userAgent)
    bing = Bing(srch_query, userAgent)

    hrefs = []
    for lnk in startpage:
        hrefs.append(lnk)
    for link in google:
        hrefs.append(link)
    for lk in bing:
        hrefs.append(lk)

    p = re.compile("\"|'")
    quote_marks = []

    for i in hrefs:
        sane = p.sub("", i)
        quote_marks.append(sane)

    print(quote_marks)

    href_set = set(quote_marks)

    results = [i for i in enumerate(href_set)]

    fig = pyfiglet.Figlet(font="larry3d")
    print(term.home + term.clear, end="")
    print(term.move_down(1) + term.salmon1(fig.renderText("search")), end="")

    for result in results:
        print(term.move_right(1) + term.bold_peachpuff(str(result)))

    sel_question = input(term.move_right(1) + term.bold_darkorange2("{**} What is your selection? "))
    if sel_question == "":
        sys.exit()
    tup = results[int(sel_question)]
    url = tup[1]

    return url


if __name__ == "__main__":
    search_engine()
