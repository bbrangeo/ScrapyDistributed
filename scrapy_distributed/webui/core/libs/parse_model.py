from json import loads


def parse_property(item, nullable=False):
    try:
        item = loads(item)
        if len(item):
            return item
        elif nullable:
            return None
        else:
            return ['']
    except ValueError:
        return ['']

