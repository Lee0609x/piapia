#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from flask import Blueprint
from app.service.auth_service import AuthService

'''
权限模块
'''

manager = Blueprint('auth', __name__)


@manager.route('/test')
def test():
    auth_service = AuthService()
    auth_service.createUser()
    return 'ok'
