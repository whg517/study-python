# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  d4
@Date: 2019/1/9 15:38
@Description:
"""

import os, time
import multiprocessing


# worker function
def worker(sign, lock):
    lock.acquire()
    print(sign, 'pid:', os.getpid())
    lock.release()
    time.sleep(1)


if __name__ == "__main__":
    # Main
    print('Main:', os.getpid())

    plist = []
    lock = multiprocessing.Lock()
    for j in range(10):
        p = multiprocessing.Process(target=worker, args=('process', lock))
        p.start()
        plist.append(p)

    p.join()
