from scrapy.item import DictItem
from scrapy import Field
import six
from time import time
from scrapy import Item


class CommonItem():
    def __init__(self, name, fields):
        keys = {}
        for field in fields:
            keys[field] = Field()
        myClass = type(str(name.capitalize() + "Item"), (Item,), keys)
        self.item = myClass()

    def get_item(self):
        return self.item
