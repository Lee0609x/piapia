#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from app.game.online_game import OnlineGame, OnlineGameFactory

'''

'''


class GameDispatcher:

    def __init__(self):
        self.context = {}

    def dispatch(self, game_name: str) -> OnlineGame:
        return self.context[game_name].get_instance()

    def register(self, name: str, game_factory: OnlineGameFactory):
        self.context[name] = game_factory


dispatcher = GameDispatcher()
