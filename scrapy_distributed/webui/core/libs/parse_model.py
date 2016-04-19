from json import loads


def parse_property(item):
    try:
        item = loads(item)
        if len(item):
            return item
        else:
            return ['']
    except ValueError:
        return ['']

