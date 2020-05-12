# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  d03
@Date: 2018/12/27 16:50
@Description:
"""

__author__ = 'wanghuagang'

import time
import requests
from twisted.internet import reactor, task


def hello(name):
    print(f'Hello world! ===> {name} ===> {str(int(time.time()))}')


def request_google():
    res = requests.get('https://www.google.com')
    return res


reactor.callWhenRunning(hello, 'yudahai')
reactor.callLater(1, request_google)

reactor.callLater(3, hello, 'yuyue')

reactor.run()
