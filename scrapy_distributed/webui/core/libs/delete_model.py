from ..models import Spider, Rule


def delete_spider(id):
    result = Spider.objects.filter(id=id).delete()
    return result


def delete_rule(id):
    result = Rule.objects.filter(id=id).delete()
    return result