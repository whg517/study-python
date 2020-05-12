# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d2
@Date: 2019/7/5 下午1:55
@Description:

"""

import signal
import sys
import time

"""
注意：在一个进程中，只能设置一个时钟，如果设置第二个则会覆盖第一个的时间，返回地一个的剩余时间，第一个闹钟返回0。
"""


def handler(signum, frame):
    print('闹钟')
    sys.exit(0)


signal.signal(signal.SIGALRM, handler)

print(signal.alarm(3))  # 0
time.sleep(1)
print(signal.alarm(4))  # 2

while True:
    time.sleep(1)
    print("学习python中...")
