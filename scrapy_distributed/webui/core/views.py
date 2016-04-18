from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Spider
from json import dumps, loads


def index(request):
    spiders = Spider.objects.order_by('updated_at')
    context = {'spiders': spiders}
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    elif request.method == 'POST':
        allowed_domains = request.POST.getlist('allowed_domains[]')

        a = dumps(allowed_domains)
        print a

        b = loads(a)
        print b

        spider = Spider(allowed_domains=a)
        print 'wwwww', spider.save()
        print spider.id

        return HttpResponse('sss')


def new(request):
    if request.method == 'POST':
        allowed_domains = request.POST.getlist('allowed_domains[]')

        a = dumps(allowed_domains)
        print a

        b = loads(a)
        print b

        spider = Spider(allowed_domains=a)
        print 'wwwww', spider.save()
        print spider.id

        return HttpResponse('sss')


def edit(request, id):
    if request.method == 'GET':
        spider = get_object_or_404(Spider, pk=id)
        context = {'spider': spider}
        return render(request, 'edit.html', context)


def update(request, id):
    if request.method == 'POST':
        spider = get_object_or_404(Spider, pk=id)
        context = {'spider': spider}
        return render(request, 'edit.html', context)


def show(request, id):
    if request.method == 'GET':
        pass
