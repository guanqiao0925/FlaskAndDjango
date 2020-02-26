#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 4:34
# @Author   : guanqiao
# TODO(guanqiao): 数据模型类
from .extend import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))