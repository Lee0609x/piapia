#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from flask import Blueprint, request
from flask_login import login_required
from loguru import logger
from threading import Condition, Thread
from app.util import response_util

'''
chat
'''

manager = Blueprint('chat', __name__)

queue = []
condition = Condition()
chatUser = []


@manager.route('/online')
@login_required
def online():
    return response_util.sse_response(chat_event_stream())


@manager.route('/push', methods=['POST'])
# @login_required
def push():
    request_param = request.get_json()
    message = request_param.get('message')
    if message is not None and message != '':
        produce(message)
    return response_util.business_success()


def chat_event_stream():
    while True:
        condition.acquire()
        print('acquire')
        if not queue:
            print('waiting')
            condition.wait()
        message = queue.pop(0)
        yield f'data: {message}\n'
        print('release')
        condition.release()


def produce(message):
    condition.acquire()
    print('p-acquire')
    queue.append(message)
    print('p-notify')
    condition.notify_all()
    print('p-release')
    condition.release()


class ChatConsumer:
    session_id = None

    def __init__(self, session_id):
        self.session_id = session_id

    def consume(self):
        while True:
            condition.acquire()


