"""Starts Scrapy's shell."""
import subprocess

import click
import isort
import snoop
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@click.command()
@click.option("-l", "--link", prompt=True)
@snoop
def scrape_shell(link):
    """
    It was used click, so you can insert
    faster the scraping url.
    """
    cmd = f"scrapy shell '{link}' --loglevel=INFO"
    subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    scrape_shell()
