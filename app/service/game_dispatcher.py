#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from app.game.online_game import OnlineGame

'''

'''


class GameDispatcher:

    def __init__(self):
        self.context = {}

    def dispatch(self, game_name: str) -> OnlineGame:
        game = type(self.game_dict[game_name], )
        return self.game_dict[game_name]


dispatcher = GameDispatcher

if __name__ == "__main__":
    test = __import__('app.game.black_jack')
    print(test)
