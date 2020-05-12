# encoding: utf-8

"""
@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  defer_8
@Date: 2019/4/3 16:12
@Description:
"""

import sys
from twisted.internet.defer import Deferred


def got_poem(poem):
    print(poem)
    from twisted.internet import reactor
    reactor.stop()


def poem_failed(err):
    print(err)
    from twisted.internet import reactor
    reactor.stop()


def poem_done(_):
    from twisted.internet import reactor
    reactor.stop()


d = Deferred()

d.addCallbacks(got_poem, poem_failed)
d.addBoth(poem_done)

from twisted.internet import reactor

reactor.callWhenRunning(d.callback, 'Another short poem.')

reactor.run()
