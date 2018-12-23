#!/usr/bin/env python
# -*-coding:utf-8-*-

import shortuuid
from websdk.cache import get_cache
from websdk.base_handler import BaseHandler as SDKBaseHandler
from tornado.web import HTTPError


class BaseHandler(SDKBaseHandler):
    def __init__(self, *args, **kwargs):
        self.new_csrf_key = str(shortuuid.uuid())
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
        # auth_key = self.get_cookie('auth_key', None)
        #
        # if not auth_key or not self.get_secure_cookie("user_id"):
        #     # 没登录，就让跳到登陆页面
        #     raise HTTPError(401, 'auth failed')


    def get_current_user(self):
        return self.get_secure_cookie("username")

    def get_current_id(self):
        return self.get_secure_cookie("user_id")

    def get_current_nickname(self):
        return self.get_secure_cookie("nickname")

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.set_status(status_code)
            return self.render('404.html')

        elif status_code == 400:
            self.set_status(status_code)
            return self.finish('bad request')

        elif status_code == 403:
            self.set_status(status_code)
            return self.finish('Sorry, you have no permission. Please contact the administrator')

        elif status_code == 500:
            self.set_status(status_code)
            return self.finish('服务器内部错误')

        elif status_code == 401:
            self.set_status(status_code)
            return self.redirect("/login/")

        else:
            self.set_status(status_code)
