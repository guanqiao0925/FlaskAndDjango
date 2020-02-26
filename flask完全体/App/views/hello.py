#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/6 0:01
# @Author   : guanqiao
# TODO(guanqiao):

from flask import Blueprint
from flask import render_template
from App.models import User, db

# 实例化蓝图
blue = Blueprint('blue', __name__)

# 设置路由
@blue.route('/')
def hello():
    return render_template('index.html', msg='今天下雪了')

# 创建表
@blue.route('/create/')
def create():
    db.create_all()
    return "创建成功"


# 删除表
@blue.route('/drop/')
def drop():
    db.drop_all()
    return "删除成功"


# 添加用户路由
@blue.route('/adduser/')
def adduser():
    user = User()
    user.id = 6
    user.name = "Tom"
    db.session.add_all([user])
    db.session.commit()
    return "创建成功"