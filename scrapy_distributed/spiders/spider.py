# -*- coding: utf-8 -*-
from scrapy.spider import CrawlSpider
import new
import logging
from scrapy import Request
from scrapy_splash import SplashRequest
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
import re
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
from scrapy_distributed.items.items import CommonItem


class CommonSpider(CrawlSpider):
    def __init__(self, spider):
        self.name = spider.name
        self.allowed_domains = spider.get_allowed_domains
        self.start_urls = spider.get_start_urls
        rule_list = []
        spider_rules = spider.rules
        for spider_rule in spider_rules:
            extractor = spider_rule.get_extractor
            rule_paras = spider_rule.get_rule_paras
            rule_list.append(Rule(LinkExtractor(**extractor),
                                  **rule_paras))
        self.rules = tuple(rule_list)
        for method in spider.get_methods:
            method_name = self.parse_method(method)
            self.extends(method_name, method)
        super(CommonSpider, self).__init__()

    def extends(self, method_name, method_str, _method=None):
        exec method_str + '''\n_method = %s''' % method_name
        self.__dict__[method_name] = new.instancemethod(_method, self, None)

    def parse_method(self, text):
        logging.debug('Spider method: ' + text)
        pattern = re.compile(u'def\s(.*?)\(self,.*?\):')
        method_name = re.search(pattern, text)
        if method_name:
            return method_name.group(1)
        else:
            return None

    def parse_start_url(self, response):
        logging.debug('Parsing start url ' + response.url)

    def create_item(self, fields):
        item = CommonItem(self.name, fields).get_item()
        return item

    def by_splash(self, request):
        request.meta['splash'] = {
            'endpoint': 'render.html',
            'args': {
                'wait': 1,
            }
        }
        logging.debug('Crawl ' + request.url + ' by splash')
        return request
