# encoding: utf-8

"""

@author: wanghuagang

@contact: kiven517@126.com

@software: 

@site: 

@file: single_threading.py

@time: 2018/8/27 17:19

@desc:

"""

__author__ = 'wanghuagang'

from time import ctime, sleep


def music(name):
    for i in range(2):
        print(f'I was listening to {name}. {ctime()}')
        sleep(1)


def move(name):
    for i in range(2):
        print(f'I was at the {name}. {ctime()}')
        sleep(5)


if __name__ == "__main__":
    music('我爱你')
    move('生化危机')
    print(f'all over {ctime()}')

"""
I was listening to 我爱你. Mon Aug 27 17:28:12 2018
I was listening to 我爱你. Mon Aug 27 17:28:13 2018
I was at the 生化危机. Mon Aug 27 17:28:14 2018
I was at the 生化危机. Mon Aug 27 17:28:19 2018
all over Mon Aug 27 17:28:24 2018

Process finished with exit code 0
"""

"""
从上述结果可以看出，在单线程执行的时候，是按照顺序一个个来的。
"""