#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from app.game.black_jack import BlackJack, GameFactory as BlackJackGameFactory
from app.service.game_dispatcher import dispatcher

'''

'''

dispatcher.register('black_jack', BlackJackGameFactory())
