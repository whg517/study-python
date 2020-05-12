# encoding: utf-8

"""

@author: wanghuagang

@contact: kiven517@126.com

@software: 

@site: 

@file: lock.py

@time: 2018/8/27 17:59

@desc:

"""

__author__ = 'wanghuagang'

import threading
from time import sleep, ctime

num = 0

lock = threading.Lock()


def add(x):
    global num, lock
    lock.acquire()
    sleep(1)
    num += x
    print(num)
    lock.release()


if __name__ == '__main__':
    print(f'start {ctime()}')
    for i in range(10):
        t = threading.Thread(target=add, args=(1,))
        t.setDaemon(True)
        t.start()
    t.join()
    print(f'end {ctime()}')
