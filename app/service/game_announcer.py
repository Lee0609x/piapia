#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

import queue

from loguru import logger

'''
游戏通讯
'''


class GameAnnouncer:

    def __init__(self):
        self.listeners = {}

    def listen(self, user_id):
        game_queue = queue.Queue(2)
        self.listeners[user_id] = game_queue
        return game_queue

    def announce(self, user_id, message):
        try:
            self.listeners[user_id].put_nowait(message)
        except queue.Full:
            logger.info(f'玩家已离线')
            self.listeners.pop(self.listeners[user_id])

    def announce_all_player(self, message):
        keys = self.listeners.keys()
        for key in keys:
            try:
                self.listeners[key].put_nowait(message)
            except queue.Full:
                logger.info(f'玩家已离线')
                self.listeners.pop(self.listeners[key])

    def get_queue(self, user_id):
        return self.listeners[user_id]
