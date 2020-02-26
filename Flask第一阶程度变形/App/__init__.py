#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/4 12:02
# @Author   : guanqiao
# TODO(guanqiao):
from flask import Flask

# from App.views import init_route
# from App.views import init_views

from App.views import first, second, init_views


def create_app():
    app = Flask(__name__)

    # 懒加载方式
    # init_route(app)

    #蓝图1
    # init_views(app=app)

    # 蓝图2
    # app.register_blueprint(first)
    # app.register_blueprint(second)

    # 蓝图3
    init_views(app=app)


    return app