# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_distributed.item import DoubanItem


class DoubanSpider(CrawlSpider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = (
        'https://movie.douban.com/top250',
    )

    rules = (
        Rule(link_extractor=LinkExtractor(allow=('/subject/\d',)), callback='parse_item'),
        Rule(link_extractor=LinkExtractor(restrict_xpaths=('//*[@id="content"]//span[@class="next"]',)),
             callback='parse_next', follow=True),
    )

    def parse_item(self, response):
        name= response.xpath('//title/text()')[0].extract()
        title = response.xpath('//title/text()')[0].extract()
        item = DoubanItem()
        item['name'] = name
        item['title'] = title
        yield item

    def parse_next(self, response):
        print response.url

    def parse_start_url(self, response):
        print response.url

