# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d3
@Date: 2019/7/5 下午2:02
@Description:

"""
import signal
import sys


def handler(signum, frame):
    print('闹钟')
    sys.exit(0)


signal.signal(signal.SIGALRM, handler)
