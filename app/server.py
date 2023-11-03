#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

import os

from flask import Flask
import settings
from app.api.auth import manager as auth_manager
from app.db.database import db

'''
flask app
'''
app = Flask(__name__, static_url_path='/')
# 蓝图注册
app.register_blueprint(auth_manager, url_prefix=f'{settings.API_PREFIX}/auth')

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
    return app.send_static_file('index.html')


def run():
    app.run(host="0.0.0.0", port=80)
