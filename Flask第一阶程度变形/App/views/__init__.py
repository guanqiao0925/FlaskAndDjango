#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 2:51
# @Author   : guanqiao
# TODO(guanqiao):


# 懒加载方式
# def init_route(app):
#     @app.route('/')
#     def hello():
#         return 'hello'



from .first_blue import first
from .second_blue import second

def init_views(app):
    app.register_blueprint(first)
    app.register_blueprint(second)