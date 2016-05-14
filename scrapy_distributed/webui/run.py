from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from orm import get_spider, get_rules
from scrapy_distributed.spiders.spider import CommonSpider

def crawl(name):
    settings =  get_project_settings()
    process = CrawlerProcess(settings)
    spider = get_spider(name)
    process.crawl(CommonSpider, spider)
    process.start()


crawl('douban')
