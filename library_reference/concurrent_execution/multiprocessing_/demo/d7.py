# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d7
@Date: 2019/7/24 上午9:09
@Description:

"""
import logging
import os
import random
import time
from multiprocessing import Process, Queue
from typing import List

from pymongo import MongoClient
from pymongo.database import Database, Collection

LOG_LEVEL = 'DEBUG'
LOG_FILE = 'add_exist_url_to_bloom.log'

logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

# FORMAT
formatter = logging.Formatter('%(asctime)s [%(module)s] %(levelname)s: %(message)s; %(filename)s:%(lineno)d')

# ConsoleHandle
console_handle = logging.StreamHandler()
console_handle.setFormatter(formatter)
console_handle.setLevel(logging.DEBUG)
logger.addHandler(console_handle)


class Migrate(object):
    """"""

    def __init__(self):
        self.client = MongoClient('mongodb://192.168.10.3:27017')
        self.db = Database(self.client, 'crawlers_shunqiwang')
        self.client = Collection(self.db, 'companys')

        self.queues = []  # type: List[Queue]

        self.sleep_rate = 10000

    def query(self):
        return self.client.find()

    def write(self, queue: Queue):
        while True:
            if not queue.empty():
                print(queue.get())
            else:
                logging.debug('Queue is empty.')

    def queue_size(self):
        """
        返回所有队列 size 之和
        :return:
        """
        size = 0
        if self.queues:
            for queue in self.queues:
                size += queue.qsize()
        return size

    def feed_queue(self):
        for item in self.query():
            """"""
            queue = random.choice(self.queues)  # type: Queue
            queue_size = self.queue_size()
            sleep = queue_size / self.sleep_rate
            if int(sleep):
                time.sleep(sleep)
                logger.debug(f'Queue: {queue_size}, query sleep: {sleep}')
            queue.put(item)

    def parallel_process(self, parallel):
        processes = []
        for i in range(parallel):
            """"""
            processes.append(Process(target=self.write, args=(self.queues[i],)))

        for i in range(parallel):
            processes[i].start()
            print('process start')

    def parallel_run(self, parallel):

        for i in range(parallel):
            self.queues.append(Queue())

        feed_queue_process = Process(target=self.feed_queue, args=())
        feed_queue_process.start()

        self.parallel_process(parallel)

    def run(self):
        """"""


if __name__ == '__main__':
    """"""
    Migrate().parallel_run(5)
