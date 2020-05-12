# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  t
@Date: 2019/1/10 10:12
@Description:
"""

__author__ = 'wanghuagang'


def add(a):
    return a + 1


def run():
    return map(add, [1, 2])


if __name__ == '__main__':
    print(len(list(map(lambda a: a+1, [1, 2]))))
