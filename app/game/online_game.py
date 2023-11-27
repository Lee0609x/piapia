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
    def join(self, user_id) -> Response:
        pass


class OnlineGameFactory:
    @abstractmethod
    def get_instance(self) -> OnlineGame:
        pass
