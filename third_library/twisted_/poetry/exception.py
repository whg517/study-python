# encoding: utf-8

"""
@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  exception
@Date: 2019/4/3 10:25
@Description:
"""
from twisted.internet import reactor


def falldown():
    raise Exception('I fall down.')


def upagain():
    print('But I get up again.')
    reactor.stop()


reactor.callWhenRunning(falldown)
reactor.callWhenRunning(upagain)

print('Starting the reactor.')
reactor.run()
