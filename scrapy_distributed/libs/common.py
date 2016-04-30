import urllib2
import re
import hashlib



def get_local_ip():
    try:
        return re.search('\d+\.\d+\.\d+\.\d+', urllib2.urlopen("http://www.ip.cn/").read()).group(0)
    except urllib2.HTTPError:
        return '127.0.0.1'


def get_ip(str):
    pattern = re.compile('(\d+.\d+.\d+.\d+)', re.S)
    result = re.search(pattern, str)
    if result:
        return result.group()
    else:
        return None


def get_hash(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()