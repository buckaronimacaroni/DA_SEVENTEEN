import scrapy


class ScrapySpider(scrapy.Spider):
    name = 'scrapy'
    allowed_domains = ['172.18.58.80']
    start_urls = ['http://172.18.58.80/']

    def parse(self, response):
        pass
