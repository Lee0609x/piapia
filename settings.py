#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

import os

'''
项目配置
'''


def project_path():
    return os.path.dirname(os.path.realpath(__file__))


# APP
SERVER_PORT = '80'
# DB
DB_FOLDER_NAME = 'sqlite'
DB_FILE_NAME = 'app.db'
DB_INIT_SQL_FILE_NAME = 'init.sql'
# LOG
LOG_FOLDER_NAME = 'logs'
LOG_LEVEL = 'INFO'
# API
API_PREFIX = '/api'
