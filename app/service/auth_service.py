#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from app.model.user import User
from app.database import db

'''
auth service
'''


class AuthService:

    def create_user(self, name, username, userpass) -> User:
        # 创建用户
        user = User(name=name, username=username, userpass=userpass)
        db.session.add(user)
        db.session.commit()
        return user

    def query_user(self, **user_info) -> User:
        # 查询用户
        return User.query.filter_by(**user_info).first()


auth_service = AuthService()
