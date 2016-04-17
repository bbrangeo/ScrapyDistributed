from django.http import HttpResponse
from django.shortcuts import render
from .models import Spider


def index(request):
    spiders = Spider.objects.order_by('updated_at')
    context = {'spiders': spiders}
    return render(request, 'index.html', context)



def new(request):
    return render(request, 'new.html')


def create(request):
    pass