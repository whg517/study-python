# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d1
@Date: 2019/9/5 下午4:04
@Description:

"""
import asyncio
import time

import requests
from apscheduler.schedulers.background import BackgroundScheduler


def ppp(x):
    print(x)


class Task(object):
    def __init__(self):
        self.error_times = 0

    def request(self, sc, job_id):
        try:
            print(requests.get('http://127.0.0.1:8000').status_code)
        except Exception as e:
            print(f'error of : {job_id}, {e}')
            self.error_times += 1
        finally:
            if self.error_times > 3:  # max error time 3, then cancel
                print(f'cancel task: {job_id}')
                sc.remove_job(job_id)


def add_jobs(sc: BackgroundScheduler):
    sc.add_job(ppp, 'interval', seconds=2, args=('111',))
    for i in range(3):
        task_id = f'task_{i}'
        sc.add_job(Task().request, 'interval', seconds=1, id=task_id, args=(sc, task_id))


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    add_jobs(scheduler)
    scheduler.start()
    asyncio.get_event_loop().run_forever()
