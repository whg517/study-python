# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  simple
@Date: 2019/7/5 下午3:58
@Description:

"""

from twisted.internet import reactor

reactor.run()

"""
Twisted是实现了Reactor模式的，因此它必然会有一个对象来代表这个reactor或者说是事件循环，
而这正是Twisted的核心。上面代码的第一行引入了reactor，第二行开始启动事件循环。

这个程序什么事情也不做。除非你通过ctrl+c来终止它，否则它会一直运行下去。

1. Twisted的reactor只有通过调用reactor.run()来启动。
2. reactor循环是在其开始的进程中运行，也就是运行在主进程中。
3。 一旦启动，就会一直运行下去。reactor就会在程序的控制下（或者具体在一个启动它的线程的控制下）。
4. reactor循环并不会消耗任何CPU的资源。
5. 并不需要显式的创建reactor，只需要引入就OK了。（reactor是Singleton）
"""
