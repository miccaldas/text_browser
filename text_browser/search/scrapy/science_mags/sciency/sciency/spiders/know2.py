from itertools import zip_longest

import scrapy
import snoop
from sciency.items import SciencyItem
from scrapy.loader import ItemLoader
from snoop import pp


class KnowSpider(scrapy.Spider):
    name = "know2"
    allowed_domains = ["undark.org"]
    start_urls = [
        "https://undark.org/2022/11/11/book-review-the-surpisingly-imprecise-history-of-measurement/",
        "https://undark.org/2022/11/25/treating-long-covid-is-rife-with-guesswork/",
    ]

    @snoop
    def parse(self, response):
        lo = SciencyItem()
        lo["title"] = response.xpath("//h1/text()").get()
        lo["text"] = response.xpath("//p/text()").getall()
        lo["author"] = response.xpath('//div[@class="display-heading byline-item byline-author"]').re("<.*>(.*)<.*><.*>")
        return lo
