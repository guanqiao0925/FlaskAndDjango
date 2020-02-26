#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 4:32
# @Author   : guanqiao
# TODO(guanqiao):

from App import create_app
from flask_script import Manager

# 实例化app
app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
