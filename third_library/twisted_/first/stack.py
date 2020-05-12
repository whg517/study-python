# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  stack
@Date: 2019/7/5 下午4:03
@Description:

"""

import traceback
from twisted.internet import reactor


def stack():
    print(f'The python stack:')
    traceback.print_stack()


reactor.callWhenRunning(stack)
reactor.run()

"""
使用 `print_stack` 打印堆栈信息。
"""