#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.database import db

'''
用户
'''


class User(db.Model, UserMixin):
    __tablename__ = 'app_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), nullable=False)
    userpass = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.userpass = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.userpass, password)
