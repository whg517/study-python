# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  t06
@Date: 2018/12/18 14:53
@Description:
"""
from asyncio.selector_events import BaseSelectorEventLoop

import asyncio

__author__ = 'wanghuagang'

host = ''
port = 6023

asyncio.get_event_loop()

if __name__ == "__main__":
    default_loop = asyncio.get_event_loop()

    default_loop.sock_sendall()

    print(default_loop)
