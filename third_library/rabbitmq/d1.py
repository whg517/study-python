# encoding: utf-8

"""
@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d1
@Date: 2019/5/14 14:50
@Description:
"""
import random
import sys
import threading
import json
import time
from datetime import datetime

import pika
import pymongo
from bson import ObjectId
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pytz import timezone

URL = 'amqp://whg:whg@192.168.12.101/whg'
QUEUE = 'test'


class CustomsJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return o.generation_time.astimezone(timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, datetime):
            return o.astimezone(timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
        else:
            return super().default(o)


def send(body):
    with pika.BlockingConnection(pika.URLParameters(URL)) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=QUEUE, durable=True)
        channel.basic_publish(exchange='',
                              routing_key=QUEUE,
                              body=body)
        # print(f'[x] Sent {body}')


if __name__ == '__main__':
    """"""
    mongo_url = 'mongodb://192.168.12.102:27017'
    mongo_db = 'company'
    mongo_col = 'items'
    client = MongoClient(mongo_url)
    database = Database(client, mongo_db)
    collection = Collection(database, mongo_col)
    cursor = collection.find(limit=10000000)
    import pytz

    flag = 0
    # for i in cursor:
    #     flag += 1
    #     if flag % 10000 == 0:
    #         print(f'flag: {flag}')
    #     send(json.dumps(i, cls=CustomsJsonEncoder))
    #
    # for i in range(0, 5):
    #     body = {
    #         "a": i,
    #         "b": "2",
    #         "c": True,
    #         "d": [1, 2, "abc"],
    #         # "e": [1, 2, "abc",  {"a": 1, 'b': None}],
    #         # "f": [{
    #         #     "xx": 0,
    #         #     "yy": 2
    #         # }, {
    #         #     "ZZ": 1.10
    #         # }, {
    #         #     "ZZ": True
    #         # }
    #         # ],
    #         # "g": {
    #         #     "qq": "222",
    #         #     "dd": "111",
    #         #     "i": i
    #         # }
    #     }
    print(time.ctime())
    for i in range(100000):
        # time.sleep(random.randint(0, 20) / 100)
        send(json.dumps({
            'id': i,
            'name': random.randint(5, 15),
            'age': random.randint(5, 15),
            'addr': 'shanghai',
            'other': '其他！' * 500000
        }))
