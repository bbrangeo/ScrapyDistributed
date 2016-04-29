import re

def get_ip(str):
    pattern = re.compile('(\d+.\d+.\d+.\d+)', re.S)
    result = re.search(pattern, str)
    if result:
        return result.group()
    else:
        return None
