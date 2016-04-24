from json import dumps
from ..models import Spider, Rule


def create_spider(request):
    name = request.POST.get('name')
    allowed_domains = request.POST.getlist('allowed_domains[]')
    start_urls = request.POST.getlist('start_urls[]')
    custom_settings = request.POST.getlist('custom_settings[]')
    crawler = request.POST.getlist('crawler[]')
    settings = request.POST.getlist('settings[]')
    logger = request.POST.get('logger')
    methods = request.POST.getlist('methods[]')
    allowed_domains = dumps(allowed_domains)
    start_urls = dumps(start_urls)
    methods = dumps(methods)
    custom_settings = dumps(custom_settings)
    crawler = dumps(crawler)
    settings = dumps(settings)
    spider = Spider(name=name, allowed_domains=allowed_domains, custom_settings=custom_settings,
                    start_urls=start_urls, methods=methods, crawler=crawler, settings=settings, logger=logger)
    return spider


def create_rule(request, spider_id):
    allow = request.POST.getlist('allow[]')
    deny = request.POST.getlist('deny[]')
    allow_domains = request.POST.getlist('allow_domains[]')
    deny_domains = request.POST.getlist('deny_domains[]')
    deny_extensions = request.POST.getlist('deny_extensions[]')
    restrict_xpaths = request.POST.getlist('restrict_xpaths[]')
    restrict_css = request.POST.getlist('restrict_css[]')
    tags = request.POST.getlist('tags[]')
    attrs = request.POST.getlist('attrs[]')
    canonicalize = request.POST.get('canonicalize', 1)
    unique = request.POST.get('unique', 1)
    process_value = request.POST.get('process_value')
    callback = request.POST.get('callback')
    cb_kwargs = request.POST.getlist('cb_kwargs[]')
    follow = request.POST.get('follow', 1)
    process_links = request.POST.get('process_links')
    process_request = request.POST.get('process_request')
    allow = dumps(allow)
    deny = dumps(deny)
    allow_domains = dumps(allow_domains)
    deny_domains = dumps(deny_domains)
    deny_extensions = dumps(deny_extensions)
    restrict_xpaths = dumps(restrict_xpaths)
    restrict_css = dumps(restrict_css)
    tags = dumps(tags)
    attrs = dumps(attrs)
    cb_kwargs = dumps(cb_kwargs)
    canonicalize = canonicalize if canonicalize else 1
    unique = unique if unique else 1
    follow = follow if follow else 1
    rule = Rule(allow=allow, deny=deny, allow_domains=allow_domains, deny_domains=deny_domains,
                deny_extensions=deny_extensions, restrict_xpaths=restrict_xpaths, restrict_css=restrict_css,
                tags=tags, attrs=attrs, canonicalize=canonicalize, unique=unique, process_value=process_value,
                callback=callback, cb_kwargs=cb_kwargs, follow=follow, process_links=process_links,
                process_request=process_request, spider_id=spider_id)
    return rule
