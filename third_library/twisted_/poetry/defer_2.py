# encoding: utf-8

"""
@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  defer_2
@Date: 2019/4/3 16:06
@Description:
"""

from twisted.internet.defer import Deferred
from twisted.python.failure import Failure


def got_poem(res):
    print('Your poem is served:')
    print(res)


def poem_failed(err):
    print('No poety for you.')


d = Deferred()

d.addCallbacks(got_poem, poem_failed)

d.errback(Failure(Exception('I have failed.')))

print('Finished')
