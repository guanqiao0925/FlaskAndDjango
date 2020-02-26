# ！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 23:59
# @Author   : guanqiao
# TODO(guanqiao):拆分setting包括数据库迁移
import os
from App import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand

# 获取环境变量
env = os.environ.get("FLASK_ENV") or "develop"

app = create_app(env)
# app = create_app()

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
