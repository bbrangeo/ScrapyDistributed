import redis


# Default values.
REDIS_URL = None
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = ''

def from_settings(settings):
    url = settings.get('REDIS_URL',  REDIS_URL)
    host = settings.get('REDIS_HOST', REDIS_HOST)
    port = settings.get('REDIS_PORT', REDIS_PORT)
    password = settings.get('REDIS_PASSWORD', REDIS_PASSWORD)

    if url:
        return redis.from_url(url)
    else:
        return redis.Redis(host=host, port=port, password=password)
