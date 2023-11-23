#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from flask import Blueprint
from flask_login import login_required

'''
21
'''

manager = Blueprint('black_jack', __name__)


@manager.route('/online')
@login_required
def online():
    pass


@manager.route('/action', methods=['POST'])
@login_required
def action():
    pass
