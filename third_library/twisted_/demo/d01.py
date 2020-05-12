# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  d01
@Date: 2018/12/27 16:43
@Description:
"""

__author__ = 'wanghuagang'
import time
from twisted.internet import reactor


def hello():
    print(f'Hello world! ===> {str(int(time.time()))}')


# reactor.callWhenRunning(hello)
# reactor.callLater(3, hello)
# reactor.run()


class A():
    x = 0

    def __init__(self):
        self.y = 1

    def add(self):
        hasattr(self.__class__, 'y')


if __name__ == '__main__':
    print(hasattr(A, 'x'))
    print(hasattr(A, 'add'))
