# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from time import time
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class CommonSpiderItem(Item):

    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    date = Field()
    host = Field()


class DoubanItem(Item):
    name = Field()


class ExampleItem(Item):
    name = Field()
    description = Field()
    link = Field()
    crawled = Field()
    spider = Field()
    url = Field()


class ExampleLoader(ItemLoader):
    default_item_class = ExampleItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()