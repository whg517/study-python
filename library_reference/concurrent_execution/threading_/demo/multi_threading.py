# encoding: utf-8

"""

@author: wanghuagang

@contact: kiven517@126.com

@software: 

@site: 

@file: multi_threading.py

@time: 2018/8/27 17:24

@desc:

"""

import threading
from time import ctime, sleep

__author__ = 'wanghuagang'

"""
在 Python 中 主线程创建了子线程。
如果主线程执行完毕，则会等待子线程完成后再结束。
"""

def music(name):
    for i in range(2):
        print(f'I was listening to {name}. {ctime()}')
        sleep(1)


def move(name):
    for i in range(2):
        print(f'I was at the {name}. {ctime()}')
        sleep(5)


threads = []

t1 = threading.Thread(target=music, args=('我爱你',))

threads.append(t1)

t2 = threading.Thread(target=move, args=('生化危机',))

threads.append(t2)

if __name__ == "__main__":
    for t in threads:
        # t.setDaemon(True)
        t.start()
        # t.join()

    print(f'all over {ctime()}')

# 情况一：
"""
I was listening to 我爱你. Mon Aug 27 17:38:31 2018
I was at the 生化危机. Mon Aug 27 17:38:31 2018
all over Mon Aug 27 17:38:31 2018
I was listening to 我爱你. Mon Aug 27 17:38:32 2018
I was at the 生化危机. Mon Aug 27 17:38:36 2018

Process finished with exit code 0
"""

"""
从上述结果中可以看到在多线程执行中，添加了两个子线程后，主线程已经结束了。在等待子线程继续执行。

任务是并行的。
"""

# 情况二：打开 t.setDaemon(True) 的注释

"""
I was listening to 我爱你. Mon Aug 27 17:40:33 2018
I was at the 生化危机. Mon Aug 27 17:40:33 2018
all over Mon Aug 27 17:40:33 2018

Process finished with exit code 0
"""

"""
从上述结果可以看出，设置setDaemon的参数为True之后。主线程和子线程会同时运行，主线程结束运行后，
无论子线程运行与否，都会和主线程一起结束。
任务是并行的

注意： setDaemon 要在 start 之前设置
"""

# 情况三：打开 t.join() 的注释

"""
I was listening to 我爱你. Mon Aug 27 17:43:16 2018
I was at the 生化危机. Mon Aug 27 17:43:16 2018
I was listening to 我爱你. Mon Aug 27 17:43:17 2018
I was at the 生化危机. Mon Aug 27 17:43:21 2018
all over Mon Aug 27 17:43:26 2018

Process finished with exit code 0
"""

"""
从上述结果可以看住在设置了 t.join() 后，主线程阻塞等待子线程执行，执行完成后再执行主线程
"""