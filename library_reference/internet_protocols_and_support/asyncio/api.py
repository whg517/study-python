# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  api
@Date: 2018/12/18 14:51
@Description:
"""

__author__ = 'wanghuagang'

from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def index():
    time.sleep(3)
    return 'Hello!'


if __name__ == '__main__':
    app.run(threaded=True)
