# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  d5
@Date: 2019/1/9 15:45
@Description:
"""
import os
import time

from scrapy import Spider
from scrapy.crawler import CrawlerProcess, CrawlerRunner

import multiprocessing

__author__ = 'wanghuagang'


class ExampleSpider(Spider):
    name = 'example'

    start_urls = ['http://www.google.com']

    def parse(self, response):
        self.logger.info(response.url)
        print(f"PID:{os.getpid()} I'm Spider!")
        time.sleep(120)


def runner(spider):
    # for i in range(10):
    #     print(f"PID: {os.getpid()} : I'm sleeping...")
    #     time.sleep(1)
    process = CrawlerProcess()
    process.crawl(spider)
    process.start()


def runner_process():
    print('Main:', os.getpid())
    p = multiprocessing.Process(target=runner, args=(ExampleSpider,))

    # p.daemon = True # 是否设置为守护进程，如果为 True 则在主进程结束后终止子进程，否则等待子进程完成。 默认值为 False 。

    p.start()
    # p.join()
    print(f"PID: {os.getpid()} : I'm finished!")


if __name__ == '__main__':
    """"""
    # runner(ExampleSpider)
    runner_process()
