#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

import random
from threading import Lock

from app.game.online_game import OnlineGame, OnlineGameFactory
from app.service.auth_service import auth_service
from app.service.game_announcer import GameAnnouncer
from app.util import response_util
from app.util.sse_message_util import format_sse_message

'''

'''

actions = ['hit', 'stand', 'surrender', 'double_down']

RANKS = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)

VALUES = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}


class Card:
    def __init__(self, rank):
        self.rank = rank


class Deck:
    def __init__(self):
        self.deck = []
        for r in RANKS:
            self.deck.append(Card(r))
        random.shuffle(self.deck)


class Dealer:
    def __init__(self, players):
        self.deck = Deck()


class BlackJack(OnlineGame):

    def __init__(self):
        self.game_announcer = GameAnnouncer()

    def play(self):

        pass

    def join(self, user_id):
        self.game_announcer.listen(user_id)
        keys = self.game_announcer.listeners.keys()
        user = auth_service.query_user(id=user_id)
        message = f'{user.name}加入了游戏，keys: {keys}'
        self.game_announcer.announce_all_player(format_sse_message(user_id=user_id, event='message', message=message))
        return response_util.sse_response(self.game_event_stream(user_id))

    def game_event_stream(self, user_id):
        while True:
            yield self.game_announcer.get_queue(user_id).get()


class GameFactory(OnlineGameFactory):

    def __init__(self):
        self.black_jack = None
        self.lock = Lock()

    def get_instance(self) -> BlackJack:
        can_start = False
        try:
            self.lock.acquire()
            if self.black_jack is None:
                # 每一个实例都是一个新的对局
                self.black_jack = BlackJack()
            else:
                can_start = True
            return self.black_jack
        finally:
            if can_start:
                self.black_jack = None
            self.lock.release()
