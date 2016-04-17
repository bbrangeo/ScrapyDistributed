from django.contrib import admin

# Register your models here.
from models import Spider
from models import Rule

admin.site.register(Spider)
admin.site.register(Rule)