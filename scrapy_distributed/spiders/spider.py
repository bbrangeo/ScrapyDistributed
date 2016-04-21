# -*- coding: utf-8 -*-
from scrapy.spider import CrawlSpider
import new

class CommonSpider(CrawlSpider):

    def __init__(self, spider, rule):
        self.name = spider.name
        self.allowed_domains = spider.get_allowed_domains
        print self.allowed_domains
        self.start_urls = spider.get_start_urls
        rule_list = []
        self.rules = tuple(rule_list)
        self.extends('parse_start_url','''def parse_start_url(self, response):print response.status''')
        super(CommonSpider, self).__init__()


    def extends(self, method_name, method_str, _method=None):
        exec method_str + '''\n_method = %s''' % method_name
        self.__dict__[method_name] = new.instancemethod(_method, self, None)



