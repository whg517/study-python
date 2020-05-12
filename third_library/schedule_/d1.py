# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d1
@Date: 2019/8/9 上午10:27
@Description:

"""

import schedule


def p(x):
    print(x)


schedule.every(1).minutes.do(p, 1)

while 1:
    schedule.run_pending()
    schedule.run_all()
