#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from flask import Blueprint, request
from flask_login import login_required, logout_user, login_user, current_user

from app.exception.business_exception import BusinessException
from app.auth import login_manager
from app.model.user import User
from app.service.auth_service import AuthService
from app.util import response_util

'''
权限模块
'''

manager = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@manager.route('/login', methods=['POST'])
def login():
    request_param = request.get_json()
    username = request_param.get('username')
    userpass = request_param.get('userpass')
    user = AuthService().queryUser(username=username)
    if not user:
        raise BusinessException(message='用户名或密码错误')
    if user.username == username and user.validate_password(userpass):
        login_user(user)
        return response_util.business_success(message='登录成功', data=dict(name=user.name, user_id=user.id))
    else:
        raise BusinessException(message='用户名或密码错误')


@manager.route('/need_login')
def need_login():
    return response_util.need_login()


@manager.route('/logout')
@login_required
def logout():
    logout_user()
    return response_util.business_success(message='退出成功')


@manager.route('/current_user')
@login_required
def get_current_user():
    return response_util.business_success(data=dict(name=current_user.name, user_id=current_user.id))


@manager.route('/test')
@login_required
def test():
    current = current_user
    print(current)
    return "ok"
