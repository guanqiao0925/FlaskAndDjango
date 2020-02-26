#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 4:36
# @Author   : guanqiao
# TODO(guanqiao): 第三方库
from flask_sqlalchemy import SQLAlchemy

# 实例化数据库  （懒加载）
db = SQLAlchemy()

def init_extend(app):
    db.init_app(app)