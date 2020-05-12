# encoding: utf-8

"""
@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  count_down
@Date: 2019/4/3 10:18
@Description:
"""
from twisted.internet import reactor


class Countdown(object):
    counter = 5

    def count(self):
        if self.counter == 0:
            reactor.stop()
        else:
            print(self.counter, '...')
            self.counter -= 1
            reactor.callLater(1, self.count)


reactor.callWhenRunning(Countdown().count)

print('Start!')
reactor.run()
print('Stop!')
