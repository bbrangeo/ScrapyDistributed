from json import loads


def parse_property(item):
    try:
        item = loads(item)
        if len(item):
            return tuple(item)
        else:
            return None
    except ValueError:
        return None

