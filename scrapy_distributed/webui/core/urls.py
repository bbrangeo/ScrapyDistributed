from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all_spiders/$', views.all_spiders, name='all_spiders'),
    url(r'^create_spider/', views.create_spider, name='create_spider'),
    url(r'^create_rule/(?P<id>[0-9]+)', views.create_rule, name='create_rule'),
    url(r'^edit_spider/(?P<id>[0-9]+)', views.edit_spider, name='edit_spider'),
    url(r'^edit_rule/(?P<id>[0-9]+)', views.edit_rule, name='edit_rule'),
    url(r'^delete_spider/(?P<id>[0-9]+)', views.delete_spider, name='delete_spider'),
    url(r'^delete_rule/(?P<id>[0-9]+)', views.delete_rule, name='delete_rule'),
    url(r'^monitor/(?P<spider_name>\w+)', views.monitor, name='monitor'),
    url(r'^items/(?P<spider_name>\w+)/(?P<hash>\w+)', views.items,name='items'),
    url(r'^items/(?P<spider_name>\w+)', views.items,name='items'),

]
