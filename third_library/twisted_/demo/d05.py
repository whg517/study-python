# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  d05
@Date: 2018/12/27 17:02
@Description:
"""
import time

import requests
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.internet import reactor, task, defer


def hello(name):
    print(f'Hello world! ===> {name} ===> {str(int(time.time()))}')


def request_google():
    try:
        result = requests.request('GET', b'http://www.google.com', )
    except Exception as e:
        print(e)
        return
    print(result)


reactor.callWhenRunning(hello, 'yudahai')

reactor.callInThread(request_google)

reactor.callWhenRunning(hello, 'yuyue')

reactor.run()
