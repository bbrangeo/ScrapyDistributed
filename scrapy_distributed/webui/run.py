from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from orm import get_spider, get_rules
from scrapy_distributed.spiders.spider import CommonSpider


settings =  get_project_settings()

process = CrawlerProcess(settings)
spider = get_spider('vxcv')

rules = get_rules(spider.name)
print spider
process.crawl(CommonSpider, spider, rules)
process.start()
