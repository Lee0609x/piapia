#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from app.model.user import User
from app.database import db

'''
auth service
'''


class AuthService:

    def createUser(self):
        # 创建用户
        db.session.add(User(name='测试用户', username='test', userpass='test'))
        db.session.commit()

    def queryUser(self, **user_info):
        # 查询用户
        return User.query.filter_by(**user_info).first()
