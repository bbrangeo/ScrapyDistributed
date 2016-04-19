from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Spider, Rule
from libs.create_model import create_spider as cs, create_rule as cr
from libs.update_model import update_spider as us, update_rule as ur


def index(request):
    spiders = Spider.objects.order_by('updated_at')
    context = {'spiders': spiders}
    return render(request, 'index.html', context)


def create_spider(request):
    if request.method == 'GET':
        return render(request, 'create_spider.html')
    elif request.method == 'POST':
        print request.POST
        spider = cs(request)
        spider.save()
        spider_id = spider.id
        return redirect(reverse('create_rule', args=[spider_id]))


def edit_spider(request, id):
    if request.method == 'GET':
        spider = get_object_or_404(Spider, pk=id)
        rules = Rule.objects.filter(spider_id=id)

        context = {'spider': spider, 'rules': rules}
        print rules
        print spider.allowed_domains
        return render(request, 'edit_spider.html', context)
    elif request.method == 'POST':
        result = us(request, id)
        print '-----', result
        if result:
            return redirect(reverse('edit_spider', args=[id]))


def create_rule(request, id):
    if request.method == 'GET':
        spider = get_object_or_404(Spider, pk=id)
        context = {'spider': spider}
        return render(request, 'create_rule.html', context)
    elif request.method == 'POST':
        get_object_or_404(Spider, pk=id)
        print request.POST
        rule = cr(request, id)
        rule.save()
        print rule.id
        return redirect(reverse('edit_rule', args=[rule.id]))



def edit_rule(request, id):
    if request.method == 'GET':
        rule = get_object_or_404(Rule, pk=id)
        spider = get_object_or_404(Spider, pk=rule.spider_id)
        context = {'spider': spider, 'rule': rule}
        return render(request, 'edit_rule.html', context)
    elif request.method == 'POST':
        get_object_or_404(Spider, pk=id)
        print request.POST
        rule = cr(request, id)
        rule.save()
        print rule.id
        return HttpResponse('sss')


def update(request, id):
    if request.method == 'POST':
        spider = get_object_or_404(Spider, pk=id)
        context = {'spider': spider}
        return render(request, 'edit.html', context)


def show(request, id):
    if request.method == 'GET':
        pass
