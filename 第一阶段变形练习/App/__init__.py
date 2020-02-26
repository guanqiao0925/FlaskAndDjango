#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 3:31
# @Author   : guanqiao
# TODO(guanqiao):

from flask import Flask

from App.views import init_views


def create_app():
    app = Flask(__name__)

    # 初始化视图
    init_views(app=app)

    return app

