#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 3:10
# @Author   : guanqiao
# TODO(guanqiao):
from flask import Blueprint

second = Blueprint('second_blue', __name__)

@second.route('/second/')
def second_blue():
    return 'second_blue'

