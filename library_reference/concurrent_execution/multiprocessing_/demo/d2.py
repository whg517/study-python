# encoding: utf-8

"""

@author: wanghuagang

@contact: kiven517@126.com

@software: 

@site: 

@file: d2.py

@time: 2018/8/27 18:24

@desc:

"""

__author__ = 'wanghuagang'
from multiprocessing import Process
import os


def info(title):
    print(title)
    print(f'model name: {__name__}')
    print(f'parent process: {os.getppid()}')
    print(f'process id: {os.getpid()}')


def f(name):
    info('function f')
    print(f'hello {name}')


if __name__ == '__main__':
    info('main line')
    print(f'pid: {os.getpid()}')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
