#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

'''
业务异常封装
'''


class BusinessException(Exception):
    message = '请求失败'

    def __init__(self, *, message):
        if message is not None:
            self.message = message

