#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/6 0:00
# @Author   : guanqiao
# TODO(guanqiao):注测蓝图
from .hello import blue

# 注测蓝图
def init_views(app):
    app.register_blueprint(blue)

