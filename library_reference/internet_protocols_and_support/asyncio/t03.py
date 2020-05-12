# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  t03
@Date: 2018/12/18 14:19
@Description:

https://blog.csdn.net/qq_42156420/article/details/81138062

"""

__author__ = 'wanghuagang'

import asyncio
import requests


async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status


def callback(task):
    print('Status', task.result())


coroutine = request()

task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)

print('Task:', task)
