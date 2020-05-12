# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  t05
@Date: 2018/12/18 14:53
@Description:
"""

__author__ = 'wanghuagang'

import asyncio
import requests
import time

start = time.time()

# async def request():
#     url = 'http://127.0.0.1:5000'
#     print('Waiting for', url)
#     response = requests.get(url)
#     print('Get response from ', url, 'Result: ', response.text)


# async def request():
#     url = 'http://127.0.0.1:5000'
#     print('Waiting for', url)
#     response = await requests.get(url)
#     print('Get response from ', url, 'Result: ', response.text)


import aiohttp


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = await response.text()
    session.close()
    return result


async def request():
    url = 'http://127.0.0.1:5000'
    print('Waiting for', url)
    response = await get(url)
    print('Get response from ', url, 'Result: ', response)


tasks = [asyncio.ensure_future(request()) for _ in range(5)]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()

print('Cast time:', end - start)
