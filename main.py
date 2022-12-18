import scrapy
from scrapy.crawler import CrawlerProcess
from CDEK.spiders import CDEK_spider

if __name__ == "__main__":
    process = CrawlerProcess()
    # (settings={
    # "FEEDS": {
    #     "out.json": {"format": "json"},
    # },
    # })

    process.crawl(CDEK_spider)
    process.start() # the script will block here until the crawling is finished