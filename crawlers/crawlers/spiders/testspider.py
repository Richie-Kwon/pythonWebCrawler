import scrapy


class TestspiderSpider(scrapy.Spider):
    name = 'testspider'
    allowed_domains = ['scrapinghub.com']
    start_urls = ['http://scrapinghub.com/']

    def parse(self, response):
        pass
