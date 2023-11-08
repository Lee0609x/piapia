#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from flask import jsonify

'''
HTTP响应工具
'''


def business_error(*, code=500, message='业务异常'):
    return jsonify(BusinessResponse(code=code, message=message).__dict__)


def business_success(*, message='请求成功', data=None):
    return jsonify(BusinessResponse(code=0, message=message, data=data).__dict__)


def need_login():
    return jsonify(BusinessResponse(code=401, message='需要登录').__dict__)


class BusinessResponse:

    def __init__(self, *, code, message, data=None):
        self.code = code
        self.message = message
        self.data = data
