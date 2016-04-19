from __future__ import unicode_literals

from django.db.models import Model, CharField, DateTimeField, ForeignKey, IntegerField, TextField
from libs.parse_model import parse_property


class Spider(Model):
    name = CharField(max_length=255)
    allowed_domains = TextField()
    start_urls = TextField()
    custom_settings = TextField()
    crawler = TextField()
    settings = TextField()
    logger = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    @property
    def get_allowed_domains(self):
        return parse_property(self.allowed_domains)

    @property
    def get_start_urls(self):
        return parse_property(self.start_urls)

    @property
    def get_custom_settings(self):
        return parse_property(self.custom_settings)

    @property
    def get_crawler(self):
        return parse_property(self.crawler)

    @property
    def get_settings(self):
        return parse_property(self.settings)

    @property
    def get_logger(self):
        return parse_property(self.logger)

    @property
    def rules(self):
        return Rule.objects.filter(spider_id=self.id)


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
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    spider = ForeignKey(Spider)

    def __unicode__(self):
        return 'xpaths: '+ self.restrict_xpaths + ' allow: ' + self.allow + ' callback: ' + self.callback

    @property
    def get_allow(self):
        print 'xxxx', self.allow
        return parse_property(self.allow)

    @property
    def get_deny(self):
        return parse_property(self.deny)

    @property
    def get_allow_domains(self):
        return parse_property(self.allow_domains)

    @property
    def get_deny_domains(self):
        return parse_property(self.deny_domains)

    @property
    def get_deny_extensions(self):
        return parse_property(self.deny_extensions)

    @property
    def get_restrict_xpaths(self):
        return parse_property(self.restrict_xpaths)

    @property
    def get_restrict_css(self):
        return parse_property(self.restrict_css)

    @property
    def get_tags(self):
        return parse_property(self.tags)

    @property
    def get_attrs(self):
        return parse_property(self.attrs)

    @property
    def get_cb_kwargs(self):
        return parse_property(self.cb_kwargs)
