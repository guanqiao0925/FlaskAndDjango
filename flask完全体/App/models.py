#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/6 0:00
# @Author   : guanqiao
# TODO(guanqiao):模型
from .extenions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))

