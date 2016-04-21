import re, urllib2


def get_local_ip():
    try:
        return re.search('\d+\.\d+\.\d+\.\d+', urllib2.urlopen("http://www.ip.cn/").read()).group(0)
    except urllib2.HTTPError:
        return '127.0.0.1'
