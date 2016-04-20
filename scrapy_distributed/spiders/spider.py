# -*- coding: utf-8 -*-
from scrapy.spider import CrawlSpider


class CommonSpider(CrawlSpider):

    def __init__(self, spider, rule):
        self.name = spider.name
        self.allowed_domains = spider.get_allowed_domains
        print self.allowed_domains
        self.start_urls = spider.get_start_urls
        rule_list = []
        self.rules = tuple(rule_list)
        super(CommonSpider, self).__init__()

    def parse_start_url(self, response):
        print response.url
