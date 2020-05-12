# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  d6
@Date: 2019/1/9 16:03
@Description:
"""

__author__ = 'wanghuagang'

from multiprocessing import Process, Queue


def f(q):
    q.put('X' * 1000000)


if __name__ == '__main__':
    queue = Queue()
    p = Process(target=f, args=(queue,))
    p.start()
    obj = queue.get()
    p.join()  # this deadlocks
