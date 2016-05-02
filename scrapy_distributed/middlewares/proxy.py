import base64
import random

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
            if proxy['user_pass'] is not None:
                request.meta['proxy'] = "http://%s" % proxy['ip_port']
                encoded_user_pass = base64.encodestring(proxy['user_pass'])
                request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
                print "**************ProxyMiddleware have pass************" + proxy['ip_port']
            else:
                print "**************ProxyMiddleware no pass************" + proxy['ip_port']
                request.meta['proxy'] = "http://%s" % proxy['ip_port']
        else:
            return request
