#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from app.database import db

'''
玩家
'''


class Player(db.Model):
    __tablename__ = 'app_player'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    coin = db.Column(db.Integer, nullable=False, default=0)
    win = db.Column(db.Integer, nullable=False, deploy=0)
    loss = db.Column(db.Integer, nullable=False, deploy=0)

    def __init__(self, user_id):
        self.user_id = user_id

