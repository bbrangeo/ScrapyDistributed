# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-21 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spider',
            name='methods',
            field=models.TextField(default=None),
        ),
    ]
