# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  __init__.py
@Date: 2019/7/5 上午11:35
@Description:

"""

import time


def spider(url: list):
    while True:
        if url:
            for i in url:
                time.sleep(2)
                print(i)
        else:
            time.sleep(5)
            print('wait ...')
