import requests
import scrapy


class ScrapySpider(scrapy.Spider):
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

    name = 'scrapy_spiders'
    start_urls = ["http://172.18.58.80/multi"]

    def start_requests(self):
        start_urls = ["http://172.18.58.80/multi"]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

