#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from flask import Blueprint, request
from flask_login import login_required

from app.service.game_dispatcher import dispatcher

'''
21
'''

manager = Blueprint('black_jack', __name__)


@manager.route('/online')
@login_required
def online():
    game_name = request.args.get('game')
    online_game = dispatcher.dispatch(game_name)
    return online_game.join()


@manager.route('/action', methods=['POST'])
@login_required
def action():
    pass
