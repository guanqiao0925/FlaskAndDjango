#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/4 12:02
# @Author   : guanqiao
# TODO(guanqiao): 蓝图方式调用views

from flask import Blueprint, render_template

# 蓝图方式
# blue = Blueprint('first', __name__)
first = Blueprint('first', __name__)

# @blue.route('/')
@first.route('/')
def first_blue():
    return render_template('first_blue.html', message='测试一个', test='测试两个')