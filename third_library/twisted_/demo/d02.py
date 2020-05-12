# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  d02
@Date: 2018/12/27 16:48
@Description:
"""

__author__ = 'wanghuagang'

import time
from twisted.internet import reactor, task


def hello(name):
    print(f'Hello world! ===> {name} ===> {str(int(time.time()))}')


task1 = task.LoopingCall(hello, 'ding')
task1.start(10)

reactor.callWhenRunning(hello, 'yudahai')
reactor.callLater(3, hello, 'yuyue')
reactor.run()
