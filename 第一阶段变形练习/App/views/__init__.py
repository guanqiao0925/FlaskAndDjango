#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 3:30
# @Author   : guanqiao
# TODO(guanqiao):

from .hello import blue


def init_views(app):

    # 注册蓝图
    app.register_blueprint(blue)

