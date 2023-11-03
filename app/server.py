#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

import os

from flask import Flask, render_template
import settings
from app.api.auth import manager as auth_manager
from app.db.database import db

'''
flask app
'''
app = Flask(__name__)
sqlite = os.path.join(settings.project_path(), settings.DB_FOLDER_NAME, settings.DB_FILE_NAME)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + sqlite
db.init_app(app)
app.register_blueprint(auth_manager, url_prefix='/auth')


@app.route('/')
def index():
    name = 'test'
    return render_template('index.html', name=name)


# 自定义错误页面
@app.errorhandler(404)
def page_404():
    return render_template('error/404.html')


@app.errorhandler(500)
def page_500():
    return render_template('error/500.html')


# 模板全局上下文
@app.context_processor
def context_map():
    return dict(gogo='gogo', go='go')


def run():
    app.run(host="0.0.0.0", port=80)
