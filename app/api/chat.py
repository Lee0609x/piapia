#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

import time
import random
import queue
from threading import Condition

from flask import Blueprint, request
from flask_login import login_required

from app.util import response_util

'''
chat
'''

manager = Blueprint('chat', __name__)

chatQueue = queue.Queue(maxsize=10)
condition = Condition()
chatUser = []


@manager.route('/online')
@login_required
def online():
    chat_id = random.randint(1, 1000)
    return response_util.sse_response(chat_event_stream(chat_id))


@manager.route('/push', methods=['POST'])
@login_required
def push():
    request_param = request.get_json()
    message = request_param.get('message')
    if message is not None and message != '':
        produce(message)
    return response_util.business_success()


def chat_event_stream(chat_id):
    while True:
        print("myId:" + str(chat_id))
        message = chatQueue.get()
        response_message = f'id: {chat_id}\nevent: chat\ndata: {message}\n\n'
        yield response_message


def produce(message):
    chatQueue.put(message)


class ChatConsumer:
    session_id = None

    def __init__(self, session_id):
        self.session_id = session_id

    def consume(self):
        while True:
            condition.acquire()
