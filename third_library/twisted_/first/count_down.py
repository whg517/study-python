# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  count_down
@Date: 2019/7/5 下午4:12
@Description:

"""
from twisted.internet import reactor


class CountDown(object):
    counter = 5

    def count(self):
        if self.counter == 0:
            reactor.stop()
        else:
            print(f'{self.counter}, ...')
            self.counter -= 1
            # 在 reactor 中注册回调函数
            # 第一个参数为几秒后执行
            # 第二个参数为回调函数引用
            reactor.callLater(1, self.count)


reactor.callWhenRunning(CountDown().count)

print('Start!')
reactor.run()
print('Stop!')
