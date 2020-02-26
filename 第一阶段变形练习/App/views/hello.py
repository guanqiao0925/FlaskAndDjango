#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 3:35
# @Author   : guanqiao
# TODO(guanqiao):

from flask import Blueprint

# 实例化蓝图
blue = Blueprint('hello', __name__)

@blue.route('/')
def hello():
    return 'hello'
