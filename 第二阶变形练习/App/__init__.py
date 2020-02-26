#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 6:17
# @Author   : guanqiao
# TODO(guanqiao):实例化app
from flask import Flask

from App.extensions import init_extend
from .views import init_views


def create_app():

    # 实例化app
    app = Flask(__name__)

    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@127.0.0.1:3306/flask_2jie'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 加载第三方库
    init_extend(app)

    # 调用蓝图
    init_views(app)

    return app