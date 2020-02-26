#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 6:16
# @Author   : guanqiao
# TODO(guanqiao):
from flask_script import Manager
from App import create_app

app = create_app()

manager = Manager(app)

if __name__ == '__main__':
    manager.run()