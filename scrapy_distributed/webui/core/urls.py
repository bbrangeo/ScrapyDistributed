from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit/(?P<id>[0-9]+)', views.edit, name='edit'),
    url(r'^update/(?P<id>[0-9]+)', views.update, name='update'),
    url(r'^create/', views.create, name='create'),
]
