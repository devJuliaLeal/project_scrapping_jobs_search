import scrapy


class TakeDataSpider(scrapy.Spider):
    name = "take_data"
    start_urls = ["https://programathor.com.br/jobs"]

    def parse(self, response):
        for jobs in response.css('.cell-list-content'):
            nome = jobs.css('.line-height-30 ::text').getall()
            if nome == 'NOVA':
                continue  # Pular para a próxima iteração do loop
            yield {
                'nome': nome,
                'tecnologia': jobs.css('.cell-list-content .background-gray ::text').getall(),
                'outrosDetalhes': jobs.css('.cell-list-content-icon span ::text').getall()
            }
