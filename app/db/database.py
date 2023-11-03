#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

import sqlite3
import os
import settings
from loguru import logger
from flask_sqlalchemy import SQLAlchemy

'''
初始化数据库
'''

db = SQLAlchemy()


def init_sqlite():
    logger.info('初始化sqlite...')
    sqlite_folder = os.path.join(settings.project_path(), settings.DB_FOLDER_NAME)
    sqlite = os.path.join(sqlite_folder, settings.DB_FILE_NAME)
    sql_script = os.path.join(sqlite_folder, settings.DB_INIT_SQL_FILE_NAME)
    if not os.path.exists(sqlite_folder):
        os.mkdir(sqlite_folder)
    if not os.path.exists(sqlite):
        logger.info('创建sqlite数据库...')
        conn = sqlite3.connect(sqlite)
        with open(sql_script, 'r', encoding='utf-8') as f:
            sql_text = f.read()
        conn.executescript(sql_text)
    else:
        pass
