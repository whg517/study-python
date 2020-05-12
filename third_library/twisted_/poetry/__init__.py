# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  __init__.py
@Date: 2019/1/9 19:00
@Description:
"""

from subprocess import run
from threading import Thread

from third_library.twisted_.poetry import slowpoetry

__author__ = 'wanghuagang'


def run_server():
    thds = []
    for i in [10000, 10001, 10002]:
        thds.append(Thread(target=run, args=(f'python slowpoetry.py --port {i} ecstasy.txt'.split(' '),)))

    for thd in thds:
        thd.start()

    for thd in thds:
        thd.join()


if __name__ == '__main__':
    """"""
    run_server()
