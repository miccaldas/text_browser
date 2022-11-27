from itertools import zip_longest

import scrapy
import snoop
from snoop import pp


class KnowSpider(scrapy.Spider):
    name = "know"
    allowed_domains = ["undark.org"]
    start_urls = [
        "https://undark.org/2022/11/11/book-review-the-surpisingly-imprecise-history-of-measurement/",
        "https://undark.org/2022/11/25/treating-long-covid-is-rife-with-guesswork/",
    ]

    @snoop
    def parse(self, response):
        mit_title = response.xpath("//h1/text()").get()
        mit_text = response.xpath("//p/text()").getall()
        mit_author_list = response.xpath("//div[@class='display-heading byline-item byline-author']").re("<.*>(.*)<.*><.*>")

        mit_author = mit_author_list[0]

        # for item in zip_longest(mit_title, mit_text, mit_author, fillvalue="missing"):
        results = {
            "title": mit_title,
            "text": mit_text,
            "author": mit_author,
        }
        yield results
