# encoding: utf-8

"""
@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d_1
@Date: 2019/4/3 10:03
@Description:
"""
from twisted.internet import reactor
import traceback


# reactor.run()

# ##############
# def hello():
#     print('Hello from the reactor loop!')
#     print('Lately I feel like I\'m stuck in a rut.')
#
#
# reactor.callWhenRunning(hello)
# print('Starting the reactor.')
# reactor.run()

# ############

def stack():
    print('The python stack:')
    traceback.print_stack()


reactor.callWhenRunning(stack)
reactor.run()
