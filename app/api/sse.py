#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

import random
import time

from flask import Blueprint
from flask_login import login_required

from app.util import response_util

'''
sse
'''

manager = Blueprint('sse', __name__)


@manager.route('/test')
@login_required
def sse_test():
    return response_util.sse_response(eventStream())


def eventStream():
    count = 0
    while True:
        count += 1
        yield 'data: %d' % count
        time.sleep(1)
