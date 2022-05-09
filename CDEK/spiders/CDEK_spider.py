import scrapy


class CdekSpiderSpider(scrapy.Spider):
    name = 'CDEK_spider'
    allowed_domains = ['cdek.shopping']
    # start_urls = ['https://cdek.shopping/products?page=1',
    #               'https://cdek.shopping/products?page=2'
    #               ]

    def start_requests(self):
        urls = [
            'https://cdek.shopping/products?page=1',
            'https://cdek.shopping/products?page=2'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass
