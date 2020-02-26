#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 4:34
# @Author   : guanqiao
# TODO(guanqiao): 注测蓝图

from .hello import blue
def init_views(app):

    # 注测蓝图
    app.register_blueprint(blue)
