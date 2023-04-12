import scrapy


class TakeDataSpider(scrapy.Spider):
    name = "take_data"
    allowed_domains = ["programathor.com.br"]
    start_urls = ["http://programathor.com.br/"]

    def parse(self, response):
        pass 
