#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

import os

from flask import Flask
import settings
from app.api.auth import manager as auth_manager
from app.auth import login_manager
from app.database import db
from loguru import logger
from flask_cors import CORS

from app.exception.business_exception import BusinessException
from app.util import response_util

'''
flask app
'''
app = Flask(__name__, static_url_path='/')
# 关闭ascii编码
app.json.ensure_ascii = False
# 蓝图注册
app.register_blueprint(auth_manager, url_prefix=f'{settings.API_PREFIX}/auth')
# 权限模块
app.secret_key = settings.SECRET_KEY
login_manager.init_app(app)
# 未登录时跳转
login_manager.login_view = f'{settings.API_PREFIX}/auth/need_login'
# CORS配置，开发环境前后端分离时使用
CORS(app, origins='http://localhost:8080')
# SQLAlchemy初始化
sqlite = os.path.join(settings.project_path(), settings.DB_FOLDER_NAME, settings.DB_FILE_NAME)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + sqlite
db.init_app(app)


@app.route('/')
def index():
    return app.send_static_file('index.html')


# 当使用前后端一体化部署，vue router使用history模式路由时，地址栏上的地址首先经过flask，未被flask路由的地址交由前端路由处理
@app.errorhandler(404)
def page_404(error):
    if settings.DEPLOY_ENV == 'prod':
        return app.send_static_file('index.html')
    else:
        return '接口不存在'


@app.errorhandler(BusinessException)
def business_exception(error):
    logger.info(f'业务异常:{error.message}')
    return response_util.business_error(message=error.message)


@app.errorhandler(Exception)
def exception(error):
    logger.exception(error)
    return response_util.business_error(message='系统异常')


def run():
    app.run(host="0.0.0.0", port=settings.SERVER_PORT)
