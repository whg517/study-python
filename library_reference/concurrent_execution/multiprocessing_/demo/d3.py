# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  d3
@Date: 2018/12/21 18:18
@Description:
"""
import time
from multiprocessing import Process

__author__ = 'wanghuagang'


def f(x):
    time.sleep(2)
    print(x * x)


if __name__ == '__main__':
    print('start')
    p = Process(target=f, args=(5,))
    p.start()
    p.join()
    print('end')
