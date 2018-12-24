#!/usr/bin/env python
# -*-coding:utf-8-*-

from websdk.base_handler import BaseHandler as SDKBaseHandler


class BaseHandler(SDKBaseHandler):
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
