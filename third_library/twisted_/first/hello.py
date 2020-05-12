# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  hello
@Date: 2019/7/5 下午4:00
@Description:

"""

from twisted.internet import reactor


def hello():
    print('Hello from the reactor loop!')
    print('Lately I fell like I\'m stuck in a rut.')


reactor.callWhenRunning(hello)

print('Starting the reactor.')

reactor.run()

"""
程序序号手动关闭


在启动 reactor `reactor.run()` 之前准备需要调用的函数。 


"""