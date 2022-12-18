import scrapy
# from fake_headers import Headers
# import cfscrape
from scrapy.crawler import CrawlerProcess
from datetime import datetime
"""
Запуск через терминал 
scrapy crawl CDEK_spider -O 50522.json

"""


class CdekSpiderSpider(scrapy.Spider):
    """
    Паука может блочить CloudFlaire
    """
    name = 'CDEK_spider'
    allowed_domains = ['cdek.shopping']
    count = 43

    # scrapy crawl CDEK_spider -o data\100522.json

    def start_requests(self):

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'cookie': '_ym_d=1652091957; _ym_uid=1652091957810149141; _ym_isad=1; _ym_visorc=b; cf_clearance=hrA3_SteOleiOXwJl5lN02lYiKhIN.1peeTIU4NADaY-1652184766-0-150; XSRF-TOKEN=eyJpdiI6Im9DU1ZyejlaV09nTUlRM2UzcmhWMWc9PSIsInZhbHVlIjoicnZFclV1amQyNGhLRStRV0VCM2d0RTB0SUlnZExsRnVlU3FtbThsMThneHB6eGYvVXl1NFErRFA3cUhyVXYweGxxYndOeGlPQ3c0MTlKbGExVERjOGU2aFFCNjA3N1VrYXRDM0tiRk5BWVdCVFZxTUMxREZUNk9wYkVlY3RqMzYiLCJtYWMiOiI1NDVlODQyYTAzNjlkNWNlODFkYTg0OGE4Nzg3MTM0YmVjODEwNjQ2ZjRmZmZhYTUxYzM1MjUxNzBlNjA3NzBkIiwidGFnIjoiIn0%3D; botble_session=eyJpdiI6IlJERjc5RWFCZHMvdXkyRUtIekVCeHc9PSIsInZhbHVlIjoiV09PNTN0ZCsrTG1aTzdhQ2l3aENtTVYxbW9XdFN4TG9vbEZOcEk2Q1BxVTVFTnJ5b2NWQ0o2U3lvd2F6WWU0cFM5Zk94VHdFUisvelFuQ1FnWXhlNnZrb0ttcDdscTJueGdrZGQ4VnVDdzdJNlFqYmxEcTh2djNiUWcvOExmK3YiLCJtYWMiOiIzNjhmN2I3OWJmNmE4NzhlYThmNmU3MWUxYTVjNTdkY2MxYmEzYjQ1Y2E4MjI4NGY2NzZlNTYzOTQ2YmE3ODdjIiwidGFnIjoiIn0%3D',
            'referer': 'https://cdek.shopping/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}

        urls = [f'https://cdek.shopping/products?page={url}' for url in range(1, self.count + 1)]
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


if __name__ == '__main__':
    current_date = datetime.today().strftime('%d%m%Y')
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        "FEEDS": {
                f"data\\{current_date}.json": {"format": "json"}, },
        'FEED_EXPORT_ENCODING': 'utf-8'
    })
    process.crawl(CdekSpiderSpider)
    process.start()
