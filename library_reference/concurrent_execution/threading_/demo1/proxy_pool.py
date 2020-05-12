# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  proxy_pool
@Date: 2019/7/5 上午11:41
@Description:

"""
import random
import time
import threading
from queue import Queue


def spider(url: Queue):
    while True:
        if not url.empty():
            # time.sleep(2)
            print(f'{time.ctime()} [spider] Crawling url: {url.get()}')
        else:
            time.sleep(5)
            print(f'{time.ctime()} [spider] wait ...')


def scheduler(bucket: Queue):
    while True:

        print(f'{time.ctime()} [scheduler] scheduling url to spider.')
        for i in range(10):
            url = f'http://www.{i}.com'
            time.sleep(random.randint(1, 3))
            bucket.put(url)
            print(f'{time.ctime()} [scheduler] put url: {url}')
        print(f'{time.ctime()} [scheduler] wait ...')
        time.sleep(10)


if __name__ == '__main__':
    """"""
    queue = Queue()
    sp = threading.Thread(target=spider, args=(queue,))
    sc = threading.Thread(target=scheduler, args=(queue,))

    sp.start()
    sc.start()

