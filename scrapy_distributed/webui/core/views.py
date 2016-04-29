from datetime import datetime
import json
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Spider, Rule
from libs.create_model import create_spider as cs, create_rule as cr
from libs.update_model import update_spider as us, update_rule as ur
from libs.delete_model import delete_spider as ds, delete_rule as dr
from scrapy_distributed.webui.core.libs.common import get_ip
from scrapy_distributed.webui.lib.settings import REDIS as redis


def index(request):
    spiders = Spider.objects.order_by('updated_at')
    context = {'spiders': spiders}
    return render(request, 'index.html', context)


def create_spider(request):
    if request.method == 'GET':
        context = {'spider': Spider()}
        return render(request, 'create_spider.html', context)
    elif request.method == 'POST':
        spider = cs(request)
        spider.save()
        spider_id = spider.id
        return redirect(reverse('create_rule', args=[spider_id]))


def edit_spider(request, id):
    if request.method == 'GET':
        spider = get_object_or_404(Spider, pk=id)
        context = {'spider': spider}
        return render(request, 'edit_spider.html', context)
    elif request.method == 'POST':
        result = us(request, id)
        if result:
            return redirect(reverse('edit_spider', args=[id]))


def delete_spider(request, id):
    if request.method == 'POST':
        result = ds(id)
        if result:
            return redirect(reverse('all_spiders', args=[]))


def all_spiders(request):
    if request.method == 'GET':
        spiders = Spider.objects.all()
        context = {'spiders': spiders}
        return render(request, 'all_spiders.html', context)


def create_rule(request, id):
    if request.method == 'GET':
        spider = get_object_or_404(Spider, pk=id)
        context = {'spider': spider, 'rule': Rule()}
        return render(request, 'create_rule.html', context)
    elif request.method == 'POST':
        get_object_or_404(Spider, pk=id)
        rule = cr(request, id)
        rule.save()
        return redirect(reverse('edit_rule', args=[rule.id]))


def edit_rule(request, id):
    if request.method == 'GET':
        rule = get_object_or_404(Rule, pk=id)
        spider = get_object_or_404(Spider, pk=rule.spider_id)
        context = {'spider': spider, 'rule': rule}
        return render(request, 'edit_rule.html', context)
    elif request.method == 'POST':
        get_object_or_404(Rule, pk=id)
        result = ur(request, id)
        if result:
            return redirect(reverse('edit_rule', args=[id]))


def delete_rule(request, id):
    if request.method == 'POST':
        result = dr(id)
        if result:
            return redirect(reverse('all_spiders', args=[]))


def monitor(request, spider_name):
    keys = redis.keys(str(spider_name + ':items:*.*'))
    print keys
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    categories = []
    data = []
    for key in keys:
        count = redis.llen(key)
        ip = get_ip(key)
        categories.append(ip)
        data.append({
            'y': count,
            'color': '#EEE'
        })
        print 'key', key, 'count', count

    context = {'categories': json.dumps(categories), 'data': data, 'title': 'Crawls results of Spider' + spider_name}

    return render(request, 'monitor.html', context)


def get_s(key):
    return ''
