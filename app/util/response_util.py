#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

import typing

from flask import jsonify, Response

import settings

'''
HTTP响应工具
'''


def business_error(*, code: int | None = 500, message: str | None = '业务异常') -> Response:
    return jsonify(BusinessResponse(code=code, message=message).__dict__)


def business_success(*, message: str | None = '请求成功', data: object | None = None) -> Response:
    return jsonify(BusinessResponse(code=0, message=message, data=data).__dict__)


def need_login() -> Response:
    return jsonify(BusinessResponse(code=401, message='需要登录').__dict__)


def sse_response(event_stream: typing.Generator) -> Response:
    if settings.DEPLOY_ENV == 'prod':
        return Response(event_stream, mimetype='text/event-stream')
    else:
        return Response(event_stream, mimetype='text/event-stream',
                        headers={'Access-Control-Allow-Credentials': 'true',
                                 'Access-Control-Allow-Origin': settings.FRONT_END_ORIGIN})


class BusinessResponse:

    def __init__(self, *, code, message, data=None):
        self.code = code
        self.message = message
        self.data = data
