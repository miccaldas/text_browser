import scrapy
import snoop
from iflscience.items import IflItem
from snoop import pp


class IflSpider(scrapy.Spider):
    name = "ifl1"
    allowed_domains = ["www.iflscience.com"]
    start_urls = [
        "http://www.iflscience.com/space-and-physics/latest?page=4",
        "http://www.iflscience.com/space-and-physics/latest?page=5",
    ]

    @snoop
    def parse(self, response):
        ii = IflItem()
        ii["title"] = response.xpath("//h1/text()").get()
        ii["text"] = response.xpath("//p/text()").getall()
        ii["author"] = response.xpath('//p[@class="author__name"]').re('<p class="author__name">(.*)</p>')
        yield ii

        next_page = response.xpath("//div[@class='card-content--body--title']/a[@href]").re('<a href="(.*)"><h3>.*</h3></a>')
        for next in next_page:
            next_page = f"https://www.iflscience.com{next}"
            yield scrapy.Request(next_page, callback=self.parse)
