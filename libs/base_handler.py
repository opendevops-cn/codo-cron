#!/usr/bin/env python
# -*-coding:utf-8-*-

import shortuuid
from websdk.cache import get_cache
from websdk.base_handler import BaseHandler as SDKBaseHandler
from tornado.web import HTTPError


class BaseHandler(SDKBaseHandler):
    def __init__(self, *args, **kwargs):
        self.new_csrf_key = str(shortuuid.uuid())
        self.user_id = None
        self.username = None
        self.nickname = None
        self.is_super = False
        self.is_superuser = self.is_super

        super(BaseHandler, self).__init__(*args, **kwargs)

    def prepare(self):

        # 验证客户端CSRF，如请求为GET，则不验证，否则验证。最后将写入新的key
        cache = get_cache()
        if self.request.method != 'GET':
            csrf_key = self.get_cookie('csrf_key')
            pipeline = cache.get_pipeline()
            result = cache.get(csrf_key, private=False, pipeline=pipeline)
            cache.delete(csrf_key, private=False, pipeline=pipeline)
            if result != '1':
                raise HTTPError(400, 'csrf error')

        cache.set(self.new_csrf_key, 1, expire=1800, private=False)
        self.set_cookie('csrf_key', self.new_csrf_key)

        ### 登陆验证
        auth_key = self.get_cookie('auth_key', None)

        if not auth_key:
            # 没登录，就让跳到登陆页面
            raise HTTPError(401, 'auth failed')
