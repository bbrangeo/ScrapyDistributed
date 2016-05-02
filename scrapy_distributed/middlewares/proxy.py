import base64
import random
import logging

PROXIES = None

class ProxyMiddleware(object):
    def __init__(self, proxies):
        self.proxies = proxies

    @classmethod
    def from_settings(cls, settings):
        proxies = settings.getlist('PROXIES', PROXIES)
        return cls(proxies)

    def process_request(self, request, spider):
        if self.proxies:
            proxy = random.choice(self.proxies)
            if hasattr(proxy, 'password') and proxy['password'] is not None:
                request.meta['proxy'] = "http://%s" % proxy['url']
                encoded_user_pass = base64.encodestring(proxy['password'])
                request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
                logging.info('Using proxy ' + proxy['url'] + ' by password ' + encoded_user_pass)
            else:
                request.meta['proxy'] = "http://%s" % proxy['url']
                logging.info('Using proxy ' + proxy['url'] + ' by no password')

        else:
            return request
