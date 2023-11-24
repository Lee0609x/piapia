#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from flask import Blueprint, request
from flask_login import login_required, current_user

from app.service.message_announcer import chat_announcer
from app.util import response_util
from app.util.sse_message_util import format_sse_message

'''
chat
'''

manager = Blueprint('chat', __name__)


@manager.route('/online')
@login_required
def online():
    user_id = current_user.id
    name = current_user.name
    return response_util.sse_response(chat_event_stream(
        format_sse_message(user_id, 'chat', f'欢迎{name}进入聊天室')))


@manager.route('/push', methods=['POST'])
@login_required
def push():
    user_id = current_user.id
    name = current_user.name
    request_param = request.get_json()
    message = request_param.get('message')
    if message is not None and message != '':
        sse_message = format_sse_message(user_id, 'chat', f'{name}：{message}')
        chat_announcer.announce(sse_message)
    return response_util.business_success()


def chat_event_stream(hello_message):
    message_queue = chat_announcer.listen()
    chat_announcer.announce(hello_message)
    while True:
        sse_message = message_queue.get()
        yield sse_message
