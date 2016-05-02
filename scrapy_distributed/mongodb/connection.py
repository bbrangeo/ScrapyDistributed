from pymongo import MongoClient

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'spider'
MONGODB_SHEET = 'sheet'

def from_settings(settings):
    host = settings.get('MONGODB_HOST', MONGODB_HOST)
    port = settings.get('MONGODB_PORT', MONGODB_PORT)
    db = settings.get('MONGODB_DB', MONGODB_DB)
    sheet = settings.get('MONGODB_SHEET', MONGODB_SHEET)
    client = MongoClient(host, port)
    db = client['db']
    sheet = db['sheet']
    if sheet:
        return sheet
    else:
        return False
