# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  d04
@Date: 2018/12/27 16:55
@Description:
"""
import time
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.internet import reactor, task, defer


def hello(name):
    print(f'Hello world! ===> {name} ===> {str(int(time.time()))}')


@defer.inlineCallbacks
def request_google():
    agent = Agent(reactor)

    try:
        result = yield agent.request('GET', b'http://www.google.com',
                                     Headers({'User-Agent': ['Twisted Web Client Example']}), None)
    except Exception as e:
        print(e)
        return
    print(result)


reactor.callWhenRunning(hello, 'yudahai')

reactor.callWhenRunning(request_google)

reactor.callWhenRunning(hello, 'yuyue')

reactor.run()
