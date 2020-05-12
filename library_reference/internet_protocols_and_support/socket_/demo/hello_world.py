# encoding: utf-8

"""
@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  hello_world
@Date: 2019/4/2 10:44
@Description:
"""

import asyncio


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


asyncio.run(main())
