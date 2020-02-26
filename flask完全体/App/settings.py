#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/2/6 0:03
# @Author   : guanqiao
# TODO(guanqiao):数据库配置  开发 测试 演示 生产环境配置
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取数据库配置url
def get_db_url(dbinfo):
    engine = dbinfo.get('ENGINE') or ""
    driver = dbinfo.get('DRIVER') or ""
    user = dbinfo.get('USER') or ""
    password = dbinfo.get('PASSWORD') or ""
    host = dbinfo.get('HOST') or ""
    port = dbinfo.get('PORT') or ""
    name = dbinfo.get('NAME') or ""
    return "{}+{}://{}:{}@{}:{}/{}" .format(engine, driver, user, password, host, port, name)

class Config:
    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 开发环境
class DevelopConfig(Config):

    DEBUG = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "12345",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "helloflask"
    }

    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)


# 测试环境
class TestingConfig(Config):

    TESTING = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "12345",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "helloflask"
    }

    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)


# 演示环境
class StagingConfig(Config):

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "12345",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "helloflask"
    }

    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)



# 生成环境
class ProductConfig(Config):

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "12345",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "helloflask"
    }

    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig,
}