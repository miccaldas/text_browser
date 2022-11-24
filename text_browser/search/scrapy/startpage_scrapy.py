"""This will automate the creation of Scrapy projects."""

import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


class ScrapyProject:
    """In this class will be represented the steps needed to setup
    a Scrapy project. Each method will be a task."""

    def __init__(self, project_name, spider_name, domain):
        self.project_name = project_name
        self.spider_name = spider_name
        self.domain = domain

    @logger.catch
    @snoop
    def project_creation(self):
        """Where will create a scrapy project in location and
        name to be defined."""

        cmd = f"scrapy startproject {self.project_name}"
        subprocess.run(cmd, shell=True)

    @logger.catch
    @snoop
    def settings_definition(self):
        """We'll deal with all the usual changes on
        the settings."""

        with open(f"{self.project_name}/{self.project_name}/settings.py", "a") as d:
            d.write("ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}")
            d.write("\n")
            d.write("\n")
            d.write('FEED_EXPORT_FIELDS = ["title", "links", "content", "images", "image_urls"]')
            d.write("\n")
            d.write('FEED_FORMAT = "csv"')
            d.write("\n")
            d.write('FEED_URI = "results.csv"')
            d.write("\n")
            d.close()

    @logger.catch
    @snoop
    def spider(self):
        """We recreate the spider definition folder."""

        class_name = f"{self.spider_name}".upper()
        with open(f"{self.project_name}/{self.project_name}/spiders/{self.spider_name}.py", "w") as f:
            f.write("import scrapy   # noqa: F401\n")
            f.write("import snoop\n")
            f.write("import isort   # noqa: F401\n")
            f.write("from itertools import zip_longest")
            f.write("\n\n")
            f.write(f"class {class_name}(scrapy.Spider):\n")
            f.write(f"    name = '{self.spider_name}'\n")
            f.write("\n")
            f.write(f'    start_urls = ["{self.domain}"]')
            f.write("\n")
            f.write(
                """
    @logger.catch
    @snoop
    def parse(self, response):
        srch_titles = response.xpath(('//h3/text()').getall()
        srch_links = response.xpath()('//div[@class="w-gl__result-url-container"]/a[@href]/text()').re('https.*\n').getall()

        for item in zip_longest(srch_titles, srch_links, fillvalue='missing'):
            results = {
                "title": item[0],
                "links": item[1],
            }

            yield results
                   """
            )


if __name__ == "__main__":
    (ScrapyProject)


scrapyproj = ScrapyProject("Startpage", "start", "https://www.startpage.com/do/search?q=scrapy+feed")
scrapyproj.project_creation()
scrapyproj.settings_definition()
scrapyproj.spider()
