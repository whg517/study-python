# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  is_daemon
@Date: 2019/7/5 下午2:14
@Description:

"""

import threading
import time

"""
threading.Thread.daemon:
初始值继承于创建线程；主线程不是守护线程，因此主线程创建的所有线程默认都是 daemon = False。

如果为 True 则为后台进程，主线程结束后程序结束，而不用等待子线程完成。
如果为 False ，主线程会等待所有子线程完成后才结束。
"""


def task():
    for i in range(10):
        time.sleep(1)
        print(i)


def daemon_true():
    t = threading.Thread(target=task, args=())
    t.setDaemon(True)
    t.start()


def daemon_false():
    """"""
    t = threading.Thread(target=task, args=())
    t.start()


if __name__ == '__main__':
    """"""
    daemon_false()