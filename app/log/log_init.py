#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

import sys
import os
from loguru import logger
import settings

'''
日志初始化
'''


def init_loguru():
    log_format = (
        '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level}</level> | [{name}:{line}] - '
        '<level>{message}</level>'
    )
    logger.remove()
    level = 'INFO'
    if settings.LOG_LEVEL not in ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'):
        pass
    else:
        level = settings.LOG_LEVEL
    logger.add(sys.stdout, level=level, format=log_format)
    logger.add(os.path.join(settings.project_path(), settings.LOG_FOLDER_NAME, 'app-{time:YYYY-MM-DD}.log'),
               level=level, format=log_format, encoding='utf-8', rotation='00:00', retention='10 days')
