from json import loads


def parse_property(item):
    if item:
        return loads(item)
    else:
        return ['']
