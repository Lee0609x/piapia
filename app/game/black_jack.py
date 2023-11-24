#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

import random

from app.game.online_game import OnlineGame
from app.service.game_announcer import GameAnnouncer
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
        self.game_announcer = GameAnnouncer()
        self.players = players
        for player in players:
            self.game_announcer.listen(player.user_id)

    def new_game(self):
        self.game_announcer.announce_all_player()


class BlackJack(OnlineGame):
    def play(self):
        pass

    def join(self):
        pass






