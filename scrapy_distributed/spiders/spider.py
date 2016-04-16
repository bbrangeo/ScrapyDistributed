# -*- coding: utf-8 -*-
from scrapy.spider import CrawlSpider


class SpiderSpider(CrawlSpider):
    name = "spider"
    allowed_domains = ["www.cuiqingcai.com"]
    start_urls = (
        'http://www.www.cuiqingcai.com/',
    )

    def parse(self, response):
        pass
