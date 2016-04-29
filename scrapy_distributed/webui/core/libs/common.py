import re

import hashlib

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