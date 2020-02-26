#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 4:34
# @Author   : guanqiao
# TODO(guanqiao): 实例化app

from flask import Flask
from .views import init_views
# from .extend import init_models
from .extend import init_extend
from flask_sqlalchemy import SQLAlchemy

def create_app():

    # 实例化app
    app = Flask(__name__)

    # url 数据库+驱动：//用户名：密码@主机：端口/库名
    # 设置链接数据库
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///sqlite.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@127.0.0.1/flask_2jie'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 加载第三方库
    init_extend(app)

    # # 调用模型
    # init_models(app)


    # 调用蓝图
    init_views(app)

    return app


