from __future__ import unicode_literals
import logging
from django.db.models import Model, CharField, DateTimeField, ForeignKey, IntegerField, TextField
from libs.parse_model import parse_property


class Spider(Model):
    name = CharField(max_length=255)
    allowed_domains = TextField()
    start_urls = TextField()
    custom_settings = TextField()
    methods = TextField(default=None)
    crawler = TextField()
    settings = TextField()
    logger = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    @property
    def get_allowed_domains(self):
        return parse_property(self.allowed_domains)

    @property
    def get_methods(self):
        return parse_property(self.methods)

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
    def get_methods(self):
        return parse_property(self.methods)

    @property
    def get_settings(self):
        return parse_property(self.settings)

    @property
    def get_logger(self):
        return parse_property(self.logger)

    @property
    def rules(self):
        return Rule.objects.filter(spider_id=self.id)

    def __unicode__(self):
        return 'name: ' + self.name + ' allowed_domains: ' + self.allowed_domains + ' start_urls: ' + self.start_urls

    def get_attr_value(self, attr):
        if hasattr(self, 'get_' + attr):
            return getattr(self, 'get_' + attr)
        elif hasattr(self, attr):
            return getattr(self, attr)
        else:
            return None


    @property
    def get_all_properties(self):
        return {
            'name': {'kind': 'text', 'value': self.get_attr_value('name'), 'display': 'Name'},
            'allowed_domains': {'kind': 'list', 'value': self.get_attr_value('allowed_domains'),
                                'display': 'Allowed Domains'},
            'start_urls': {'kind': 'list', 'value': self.get_attr_value('start_urls'), 'display': 'Start Urls'},
            'custom_settings': {'kind': 'list', 'value': self.get_attr_value('custom_settings'),
                                'display': 'Custom Settings'},
            'crawler': {'kind': 'list', 'value': self.get_attr_value('crawler'), 'display': 'Crawler'},
            'settings': {'kind': 'list', 'value': self.get_attr_value('settings'), 'display': 'Settings'},
            'logger': {'kind': 'text', 'value': self.get_attr_value('logger'), 'display': 'Logger'},
            'methods': {'kind': 'list_area', 'value': self.get_attr_value('methods'), 'display': 'Methods'},
        }


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

    def get_dict(self, attrs):
        attr_dict = {}
        for attr in attrs:
            value = self.get_attr_value(attr)
            if isinstance(value, (tuple, )):
                if len(value) > 0 and value[0]:
                    attr_dict[attr] = value
            elif isinstance(value, (long, )):
                attr_dict[attr] = value
            elif value:
                attr_dict[attr] = value
        return attr_dict

    @property
    def get_extractor(self):

        attrs = ['allow', 'deny', 'allow_domains',
                 'deny_domains', 'deny_extensions',
                 'restrict_xpaths', 'restrict_css',
                 'tags', 'attrs', 'canonicalize',
                 'unique', 'process_value'
                 ]
        dict = self.get_dict(attrs)
        logging.debug('Rule extractor: ' + str(dict))
        return dict

    @property
    def get_rule_paras(self):
        attrs = ['callback', 'cb_kwargs', 'follow',
                 'process_links', 'process_request']
        dict = self.get_dict(attrs)
        logging.debug('Rule para: ' + str(dict))
        return dict

    def get_attr_value(self, attr):
        if hasattr(self, 'get_' + attr):
            return getattr(self, 'get_' + attr)
        elif hasattr(self, attr):
            return getattr(self, attr)
        else:
            return None

    def __unicode__(self):
        return 'xpaths: ' + self.restrict_xpaths + ' allow: ' + self.allow + ' callback: ' + self.callback

    @property
    def get_allow(self):
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

    @property
    def get_all_properties(self):
        return {
            'allow': {'kind': 'list', 'value': self.get_attr_value('allow'), 'display': 'Allow'},
            'deny': {'kind': 'list', 'value': self.get_attr_value('deny'), 'display': 'Deny'},
            'allow_domains': {'kind': 'list', 'value': self.get_attr_value('allow_domains'),
                              'display': 'Allow Domains'},
            'deny_domains': {'kind': 'list', 'value': self.get_attr_value('deny_domains'), 'display': 'Deny Domains'},
            'deny_extensions': {'kind': 'list', 'value': self.get_attr_value('deny_extensions'),
                                'display': 'Deny Extensions'},
            'restrict_xpaths': {'kind': 'list', 'value': self.get_attr_value('restrict_xpaths'),
                                'display': 'Restrict Xpaths'},
            'restrict_css': {'kind': 'list', 'value': self.get_attr_value('restrict_css'), 'display': 'Restrict CSS'},
            'tags': {'kind': 'list', 'value': self.get_attr_value('tags'), 'display': 'Tags'},
            'attrs': {'kind': 'list', 'value': self.get_attr_value('attrs'), 'display': 'Attrs'},
            'canonicalize': {'kind': 'number', 'value': self.get_attr_value('canonicalize'), 'display': 'Canonicalize'},
            'unique': {'kind': 'number', 'value': self.get_attr_value('unique'), 'display': 'Unique'},
            'process_value': {'kind': 'text', 'value': self.get_attr_value('process_value'),
                              'display': 'Process Value'},
            'callback': {'kind': 'text', 'value': self.get_attr_value('callback'), 'display': 'Callback'},
            'cb_kwargs': {'kind': 'list', 'value': self.get_attr_value('cb_kwargs'), 'display': 'Cb Kwargs'},
            'follow': {'kind': 'number', 'value': self.get_attr_value('follow'), 'display': 'Follow'},
            'process_links': {'kind': 'text', 'value': self.get_attr_value('process_links'),
                              'display': 'Process Links'},
            'process_request': {'kind': 'text', 'value': self.get_attr_value('process_request'),
                                'display': 'Process Request'},
        }
