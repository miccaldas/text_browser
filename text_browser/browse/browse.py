"""
This script imports a module that searches Startpage
Google and Bing for a query, the user chooses one result,
and here it is opened in Glow.

"""
import subprocess

# import snoop
# from snoop import pp

from text_browser.search import search_engine


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def get_request():
    """
    We're basically calling two cli apps to do all
    the work. Pandoc downloads and converts a page
    from HTML to Markdown. Glow views it..
    """

    url = search_engine.search_engine()
    output = "content.md"

    cmd = f"pandoc --columns=100 -o {output} --wrap=auto -f html -t markdown {url}"
    subprocess.run(cmd, shell=True)

    cmd1 = "glow -s /home/mic/glamour/styles/mic.json"
    subprocess.run(cmd1, cwd="/home/mic/python/text_browser/text_browser/browse", shell=True)


if __name__ == "__main__":
    get_request()
