#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 6:17
# @Author   : guanqiao
# TODO(guanqiao):注测蓝图
from .hello import blue

def init_views(app):
    app.register_blueprint(blue)

