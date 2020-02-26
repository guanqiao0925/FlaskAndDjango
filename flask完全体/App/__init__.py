#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 23:59
# @Author   : guanqiao
# TODO(guanqiao):实例化app

from flask import Flask

from App.settings import get_db_url, envs
from .extenions import init_extenions
from .views import init_views

# 实例化app
def create_app(env):

    app = Flask(__name__)

    # 初始化项目配置
    app.config.from_object(envs.get(env))
    # app.config.from_object(envs.get('develop'))

    # 初始化非路由相关扩展库
    init_extenions(app)

    # 初始化路由
    init_views(app)

    return app