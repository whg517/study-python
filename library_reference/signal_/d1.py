# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d1
@Date: 2019/7/5 下午1:51
@Description:

"""

import signal
import sys
import time

"""
signal.SIGHUP   # 连接挂断;
signal.SIGILL   # 非法指令;
signal.SIGINT   # 终止进程（ctrl+c）;
signal.SIGTSTP  # 暂停进程（ctrl+z）;
signal.SIGKILL  # 杀死进程（此信号不能被捕获或忽略）;
signal.SIGQUIT  # 终端退出;
signal.SIGTERM  # 终止信号,软件终止信号;
signal.SIGALRM  # 闹钟信号,由signal.alarm()发起;
signal.SIGCONT  # 继续执行暂停进程;
"""


def handler(signum, frame):
    print('闹钟')
    sys.exit(0)


signal.signal(signal.SIGALRM, handler)

signal.alarm(4)  # 4s后终止程序

while True:
    time.sleep(1)
    print("学习python中...")

