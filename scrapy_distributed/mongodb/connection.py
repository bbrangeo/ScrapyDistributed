from pymongo import MongoClient



# Default values.
MONGODB_URL = None
MONGODB_HOST = 'localhost'
MONGODB_USER = 'root'
MONGODB_PASSWORD = ''

def from_settings(settings):
    url = settings.get('MONGODB_URL',  MONGODB_URL)
    host = settings.get('MONGODB_HOST', MONGODB_HOST)
    user = settings.get('MONGODB_USER', MONGODB_USER)
    password = settings.get('MONGODB_PASSWORD', MONGODB_PASSWORD)

    if url:
        return MongoClient(url)
    else:
        url = 'mongodb://{0}:{1}@{2}'.format(user, password, host)
        return MongoClient(url)
