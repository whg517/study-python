# encoding: utf-8

"""
@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  defer_1
@Date: 2019/4/3 15:44
@Description:
"""

from twisted.internet.defer import Deferred


def got_poem(res):
    print('Your poem is served:')
    print(res)


def poem_failed(err):
    print('No poetry for you.')


d = Deferred()

d.addCallbacks(got_poem, poem_failed)

d.callback('This poem is short.')

print('Finished.')
