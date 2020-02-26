#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/6 0:00
# @Author   : guanqiao
# TODO(guanqiao):第三方库
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
# 加载第三方库  使用懒加载方式
def init_extenions(app):
    db.init_app(app=app)
    migrate.init_app(app, db)


