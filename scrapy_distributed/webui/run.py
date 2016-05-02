from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from orm import get_spider, get_rules
from scrapy_distributed.spiders.spider import CommonSpider

def crawl(name):
    settings =  get_project_settings()
    process = CrawlerProcess(settings)
    spider = get_spider(name)
    rules = get_rules(spider.name)
    process.crawl(CommonSpider, spider, rules)
    process.start()


crawl('douban2')
