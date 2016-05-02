from twisted.internet.threads import deferToThread
from . import connection

class MongodbPipeline(object):

    def __init__(self, client):
        self.client = client

    @classmethod
    def from_settings(cls, settings):
        client = connection.from_settings(settings)
        return cls(client)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def process_item(self, item, spider):
        return deferToThread(self._process_item, item, spider)

    def _process_item(self, item, spider):
        self.client.insert_one(dict(item))
        return item
