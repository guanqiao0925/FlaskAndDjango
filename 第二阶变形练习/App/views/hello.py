#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 6:18
# @Author   : guanqiao
# TODO(guanqiao):实例化蓝图
from flask import Blueprint
from App.models import db

# 实例化蓝图
blue = Blueprint('blue', __name__)

# 设置创建数据表路由
@blue.route('/')
def createdb():

    db.create_all()
    return '创建成功'
