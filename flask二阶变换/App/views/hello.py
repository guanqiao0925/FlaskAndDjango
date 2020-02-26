#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 4:36
# @Author   : guanqiao
# TODO(guanqiao): 实例化蓝图

from flask import Blueprint, render_template

# 实例化蓝图
from App.models import db

blue = Blueprint('hello', __name__)

# 设置路由
@blue.route('/')
def hello():
    return render_template('hello.html', msg='hello world')

# 创建数据库路由
@blue.route('/createdb/')
def createdb():

    # 创建表
    db.create_all()
    return '创建成功'