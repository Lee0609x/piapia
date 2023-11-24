#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lee0609x@163.com'

from abc import abstractmethod

from flask import Response

'''

'''


class OnlineGame:
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def join(self) -> Response:
        pass
