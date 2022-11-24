from itertools import zip_longest

import scrapy
import snoop
from snoop import pp


class KnowSpider(scrapy.Spider):
    name = "know"
    allowed_domains = ["undark.org"]
    start_urls = ["https://undark.org/2022/11/11/book-review-the-surpisingly-imprecise-history-of-measurement/"]

    @snoop
    def parse(self, response):
        mit_title = response.xpath("//h1/text()").get()
        mit_text = response.xpath("//p/text()").getall()
        mit_author = response.xpath("//span[@class='byline-label']/span/a/text()").getall()

        for item in zip_longest(mit_title, mit_text, mit_author, fillvalue="missing"):
            results = {
                "mit_title": pp(item[0]),
                "mit_text": pp(item[1]),
                "mit_author": pp(item[2]),
            }
            yield results
