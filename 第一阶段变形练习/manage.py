#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 3:29
# @Author   : guanqiao
# TODO(guanqiao):
from App import create_app
from flask_script import Manager


app = create_app()
manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()

