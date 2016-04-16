# -*- coding: utf-8 -*-
from scrapy.utils.project import get_project_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

settings = get_project_settings()


def get_mysql_engine():
    mysql_url = settings.get('MYSQL_URL')
    if mysql_url:
        return create_engine(mysql_url)
    else:
        host = settings.get('MYSQL_HOST', 'localhost')
        port = settings.get('MYSQL_PORT', 3306)
        encoding = settings.get('MYSQL_ENCODING', 'utf8')
        database = settings.get('MYSQL_DATABASE', 'scrapy_distributed')
        username = settings.get('MYSQL_USERNAME', 'root')
        password = settings.get('MYSQL_PASSWORD', '')
        mysql_url = 'mysql+mysqldb://{0}:{1}@{2}:{3}/{4}?charset={5}'.format(username, password, host, port, database,
                                                                             encoding)
    return create_engine(mysql_url)


def get_mysql_session():
    mysql_engine = get_mysql_engine()
    return sessionmaker(bind=mysql_engine)
