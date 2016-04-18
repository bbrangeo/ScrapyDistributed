from json import loads
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Spider, Rule
from libs.create_model import create_spider, create_rule


def index(request):
    spiders = Spider.objects.order_by('updated_at')
    context = {'spiders': spiders}
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    elif request.method == 'POST':
        print request.POST
        spider = create_spider(request)
        spider.save()
        spider_id = spider.id
        rule = create_rule(request, spider_id)
        rule.save()
        print rule.id
        return HttpResponse('sss')


def edit(request, id):
    if request.method == 'GET':
        spider = get_object_or_404(Spider, pk=id)
        rules = Rule.objects.filter(spider_id=id)

        context = {'spider': spider, 'rules': rules}
        print rules
        print spider.allowed_domains
        return render(request, 'edit.html', context)

    elif request.method == 'POST':
        pass


def update(request, id):
    if request.method == 'POST':
        spider = get_object_or_404(Spider, pk=id)
        context = {'spider': spider}
        return render(request, 'edit.html', context)


def show(request, id):
    if request.method == 'GET':
        pass
