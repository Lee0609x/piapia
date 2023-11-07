#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from loguru import logger

import settings
import argparse
from app.db.sqlite import init_sqlite
from app.log.log_init import init_loguru
from app import server

'''
应用启动脚本
'''


if __name__ == '__main__':
    init_loguru()
    parser = argparse.ArgumentParser()
    parser.add_argument('--DEPLOY_ENV', type=str, default=settings.DEPLOY_ENV)
    settings.DEPLOY_ENV = parser.parse_args().DEPLOY_ENV
    logger.info(f'部署环境:{settings.DEPLOY_ENV}')
    logger.info('数据库初始化...')
    init_sqlite()
    logger.info('flask启动...')
    server.run()
