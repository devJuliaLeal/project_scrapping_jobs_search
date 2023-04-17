import scrapy


class TakeDataSpider(scrapy.Spider):
    name = "take_data"
    start_urls = ["https://programathor.com.br/jobs/page/2"]

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
        prox_pag = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "page-item", " " )) and (((count(preceding-sibling::*) + 1) = 9) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "page-link", " " ))]').attrib['href']
        if prox_pag is not None:
            yield response.follow(prox_pag, callback=self.parse)
            meta = {'ignore': True}
            yield response.follow(prox_pag, meta=meta, callback=self.parse)
