# -*- coding: utf-8 -*-
import os
import django

os.sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lib.settings")
django.setup()

from core.models import Spider

def get_all_spiders():
    return Spider.objects.all()


def get_spider(name):
    spiders =  Spider.objects.filter(name=name)
    if len(spiders):
        return spiders[0]
    else:
        return None

def get_rules(spider_name, num=0):
    spider = get_spider(spider_name)
    if not spider:
        return None
    rules = spider.rules
    if num:
        if len(rules) > num:
            return rules[num]
    else:
        return rules
