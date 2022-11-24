from itertools import zip_longest

import scrapy

from ..items import EasyItem


class VeryEasy(scrapy.Spider):
    name = "very"
    start_urls = ["https://www.startpage.com/do/search?q=python+tui+platform"]

    def parse(self, response):
        easy_item = EasyItem()

        title = response.xpath("//h1").getall()
        links = response.xpath("//cite").getall()
        # teste = response.xpath("/html/body/main/div/div[3]/div/div[1]/div[3]/p[2]/a").getall()

        for i in zip_longest(links, title, fillvalue="missing"):
            results = {
                "links": i[0],
                "title": i[1],
            }
            yield results
