#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
Author : shenshuo
date   : 2017年10月17日17:23:19
role   : 数据库连接
update : 2019年9月3日 修改为不用链接池
"""
import pymysql
from sqlalchemy.pool import NullPool
from urllib.parse import quote_plus
from settings import settings


def get_db_url(dbkey):
    databases = settings.get('databases', 0)
    db_conf = databases[dbkey]
    dbuser = db_conf['user']
    dbpwd = db_conf['pwd']
    dbhost = db_conf['host']
    dbport = db_conf.get('port', 3306)
    dbname = db_conf['name']

    return 'mysql+pymysql://{user}:{pwd}@{host}:{port}/{dbname}?charset=utf8'.format(user=dbuser, pwd=quote_plus(dbpwd),
                                                                                     host=dbhost, port=dbport,
                                                                                     dbname=dbname, poolclass=NullPool)
