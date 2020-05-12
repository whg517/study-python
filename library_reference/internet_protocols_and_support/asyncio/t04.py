# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  t04
@Date: 2018/12/18 14:26
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


tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('Tasks:', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task Result:', task.result())
