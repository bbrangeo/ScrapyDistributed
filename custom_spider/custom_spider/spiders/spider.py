# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["www.cuiqingcai.com"]
    start_urls = (
        'http://www.www.cuiqingcai.com/',
    )

    def parse(self, response):
        pass
