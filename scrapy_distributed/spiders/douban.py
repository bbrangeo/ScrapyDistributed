# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class DoubanSpider(CrawlSpider, Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = (
        'https://movie.douban.com/top250',
    )

    rules = (
        Rule(link_extractor=LinkExtractor(allow=('/subject/\d',)), callback='parse_item',
             process_links='process_links'),
        Rule(link_extractor=LinkExtractor(restrict_xpaths=('//*[@id="content"]//span[@class="next"]',)),
             callback='parse_next', follow=True),
    )

    def make_requests_from_url(self, url):
        request = Request(url, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
            'upgrade-insecure-requests': 1,
            'host': 'movie.douban.com'
        })
        return request

    def parse_item(self, response):
        print response.xpath('//title/text()')[0].extract()

    def parse_next(self, response):
        print response.url

    def process_links(self, links):
        return links
