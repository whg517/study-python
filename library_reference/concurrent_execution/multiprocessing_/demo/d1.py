# encoding: utf-8

"""

@author: wanghuagang

@contact: kiven517@126.com

@software: 

@site: 

@file: d1.py

@time: 2018/8/27 18:09

@desc:

"""

"""
multiprocessing是一个和threading模块类似，提供API，生成进程的模块。multiprocessing包提供本地和远程并发，
通过使用子进程而不是线程有效地转移全局解释器锁。
因此，multiprocessing模块允许程序员充分利用给定机器上的多个处理器。
它在Unix和Windows上都可以运行。
"""

__author__ = 'wanghuagang'

from multiprocessing import Pool


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
