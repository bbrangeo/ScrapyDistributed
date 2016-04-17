from __future__ import unicode_literals

from django.db.models import Model, CharField, DateTimeField, ForeignKey, IntegerField, TextField


class Spider(Model):
    name = CharField(max_length=255)
    allowed_domains = TextField()
    start_urls = TextField()
    custom_settings = TextField()
    crawler = TextField()
    settings = TextField()
    logger = CharField(max_length=255)
    updated_at = DateTimeField()


class Rule(Model):
    allow = TextField()
    deny = TextField()
    allow_domains = TextField()
    deny_domains = TextField()
    deny_extensions = TextField()
    restrict_xpaths = TextField()
    restrict_css = TextField()
    tags = TextField()
    attrs = TextField()
    canonicalize = IntegerField(default=1)
    unique = IntegerField(default=1)
    process_value = CharField(max_length=255)
    callback = CharField(max_length=255)
    cb_kwargs = TextField()
    follow = IntegerField(default=0)
    process_links = CharField(max_length=255)
    process_request = CharField(max_length=255)
    updated_at = DateTimeField()
    spider = ForeignKey(Spider)
