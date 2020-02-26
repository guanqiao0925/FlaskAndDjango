#！/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/1/26 0:47
# @Author   : guanqiao
# TODO(guanqiao):

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def run():
    return 'hello world'

if __name__ == '__main__':
    uvicorn.run(app=app,
                host='192.168.1.16',
                port=8080,
                workers=1
                )