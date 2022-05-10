import scrapy


class CdekSpiderSpider(scrapy.Spider):
    name = 'CDEK_spider'
    allowed_domains = ['cdek.shopping']
    count = 49
    # scrapy crawl CDEK_spider -o data\100522.json

    def start_requests(self):
        # urls = [
        #     'https://cdek.shopping/products?page=1',
        #     'https://cdek.shopping/products?page=2'
        # ]
        urls = [f'https://cdek.shopping/products?page={url}' for url in range(1, self.count)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for product in response.css('div.ps-product'):
            yield {
                'title': product.css('a.ps-product__title::text').extract(),
                'price': product.css('p.ps-product__price ::text').extract(),
                'vendor': product.css('p.ps-product__vendor a span::text').extract(),
                'badge': product.css('span.ps-product__badge::text').extract(),
                'link': product.css('a.ps-product__title::attr(href)').extract(),
                'id': product.css('a.add-to-cart-button::attr(data-id)').extract()
                # print(dict(title=title, price=price, vendor=vendor, badge=badge, link=link, id=id))
            }
