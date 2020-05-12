# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  t01
@Date: 2018/12/18 13:53
@Description:

https://blog.csdn.net/qq_42156420/article/details/81138062

"""

__author__ = 'wanghuagang'

import asyncio


async def execute(x):
    print("Number:", x)


coroutine = execute(1)

print('Coroutine:', coroutine)
print('After calling execute')

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)
print('After calling loop')

