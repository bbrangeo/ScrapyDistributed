from scrapy.utils.serialize import ScrapyJSONEncoder
from twisted.internet.threads import deferToThread

from . import connection


class MongodbPipeline(object):

    def __init__(self, server):
        self.server = server
        self.encoder = ScrapyJSONEncoder()

    @classmethod
    def from_settings(cls, settings):
        server = connection.from_settings(settings)
        return cls(server)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def process_item(self, item, spider):
        return deferToThread(self._process_item, item, spider)

    def _process_item(self, item, spider):
        key = self.item_key(item, spider)
        ip_key = self.item_ip_key(item, spider)
        data = self.encoder.encode(item)
        self.server.lpush(key, data)
        self.server.lpush(ip_key, data)
        return item

    def item_key(self, item, spider):
        return "%s:items:all" % spider.name

    def item_ip_key(self, item, spider):
        return "%s:items:%s" % (spider.name, item['ip'])
