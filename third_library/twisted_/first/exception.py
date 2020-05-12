# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  exception
@Date: 2019/7/5 下午4:19
@Description:

"""

from twisted.internet import reactor


def fall_down():
    raise Exception('I fall down.')


def up_again():
    print('But I get up again.')
    reactor.stop()


reactor.callWhenRunning(fall_down)
reactor.callWhenRunning(up_again)

print('Starting the reactor.')
reactor.run()

"""
即使第一个函数引发异常
但是第二个函数依然可以执行
如果第二个函数没有 `reactor.stop()` 的话，程序依然会继续运行  

"""