#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/4 12:01
# @Author   : guanqiao
# TODO(guanqiao):

from flask import Flask
from flask_script import Manager
from App import create_app

app = create_app()
manager = Manager(app=app)



if __name__ == '__main__':
    manager.run()