"""
Searches, in Bing and Google,
for a query made by the user.
"""
import click
import isort
import pyfiglet
import questionary
import snoop
from blessed import Terminal
from questionary import Style
from ScrapeSearchEngine.ScrapeSearchEngine import Google, Startpage
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

    results = []
    for idx, lnk in enumerate(startpage):
        results.append((idx, lnk))
    for count, link in enumerate(google, start=10):
        results.append((count, link))

    fig = pyfiglet.Figlet(font="larry3d")
    print(fig.renderText("search"))

    for result in results:
        print(result)

    sel = input("What is your selection? ")
    selection = int(sel)
    tup = results[selection]
    url = tup[1]

    return url


if __name__ == "__main__":
    search_engine()
