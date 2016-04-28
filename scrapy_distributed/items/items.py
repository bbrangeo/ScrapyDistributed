from scrapy import Field
from scrapy import Item
from datetime import datetime
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class CommonItem():
    def __init__(self, name, fields):
        keys = {}
        for field in fields:
            keys[field] = Field()
        keys['time'] = Field()
        keys['ip'] = Field()
        myClass = type(str(name.capitalize() + "Item"), (Item,), keys)
        self.item = myClass()
        now = datetime.now()
        self.item['time'] = now.strftime("%Y-%m-%d %H:%M:%S")
        self.item['ip'] = settings.get('LOCAL_IP', 'Unknown')

    def get_item(self):
        return self.item
