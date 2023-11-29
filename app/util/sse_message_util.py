#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

'''
sse报文组装
'''


def format_sse_message(user_id: int | None = 0, event: str | None = 'default', message: str | None = '') -> str:
    return f'id: {user_id}\nevent: {event}\ndata: {message}\n\n'
