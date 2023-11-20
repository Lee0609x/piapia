#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

import queue

from loguru import logger

'''
消息广播队列
'''


class MessageAnnouncer:
    listeners = []

    def listen(self, queue_size=5):
        chat_queue = queue.Queue(queue_size)
        self.listeners.append(chat_queue)
        return chat_queue

    def announce(self, message):
        # 顺序添加，倒序通知，队列阻塞时，删除旧的监听
        for index in reversed(range(len(self.listeners))):
            try:
                self.listeners[index].put_nowait(message)
            except queue.Full:
                logger.info(f'消息队列已满，清理监听，index:{index}')
                del self.listeners[index]


chat_announcer = MessageAnnouncer()
