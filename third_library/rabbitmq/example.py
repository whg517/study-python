# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  example
@Date: 2019/8/2 下午4:11
@Description:

"""

import json
import logging
import random
import string
import sys
import threading
import traceback
from datetime import datetime
import uuid

import pika

LEVEL = 'DEBUG'
logger = logging.getLogger(__file__)
logger.setLevel(LEVEL)

formatter = logging.Formatter('%(asctime)s [%(module)s] %(levelname)s: %(message)s; %(filename)s:%(lineno)d')

console_handle = logging.StreamHandler()
console_handle.setFormatter(formatter)
console_handle.setLevel(logging.DEBUG)
logger.addHandler(console_handle)


def receive():
    with pika.BlockingConnection(pika.URLParameters(URL)) as conn:
        channel = conn.channel()
        channel.queue_declare(queue=QUEUE, durable=True)
        channel.basic_consume(queue=QUEUE,
                              auto_ack=True,
                              on_message_callback=callback)
        print(f'[*] Waiting for messages, To exit press CTRL+C')
        channel.start_consuming()


def callback(ch, method, properties, body):
    print(f'[x] Received {body}')


class RabbitHelper(object):

    def __init__(self, rabbit_url, queue_name, durable):
        self.queue_name = queue_name

        self.connection = pika.BlockingConnection(pika.URLParameters(rabbit_url))

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name, durable=durable)

    def publish(self, body: str):
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue_name,
                                   body=body)

    def close(self):
        self.connection.close()


def get_random_str(length):
    str_list = []
    for i in range(length):
        str_list.extend(list(string.printable))
    random.shuffle(str_list)
    return ''.join(str_list)


class ExampleProduct(object):
    """"""

    def __init__(self, rabbit_url, queue_name, durable=True):
        self.client = RabbitHelper(rabbit_url, queue_name, durable)

        self.strategies = [
            [2018, 1, 15, 1520],
            [2018, 1, 16, 2260],
            [2018, 1, 17, 3578],
        ]

        self.total_count = 0

    def show_total_count(self):
        self.total_count += 1
        if not self.total_count % 1000:
            logger.info(self.total_count)

    def generator(self):
        for strategy in self.strategies:
            print(strategy)
            strategy_length = strategy[-1]
            count = 0
            while True:
                count += 1
                self.show_total_count()
                if count >= strategy_length:
                    break
                yield self.sample_date(strategy)

    def sample_date(self, strategy):

        return {
            'id': str(uuid.uuid1()),
            'swap_date': [strategy[0], strategy[1], strategy[2]],
            'data': get_random_str(1000)
        }

    def run(self):

        for item in self.generator():
            try:
                self.client.publish(json.dumps(item))
            except Exception as e:
                traceback.print_stack()
        self.client.close()


if __name__ == '__main__':
    """"""
    URL = 'amqp://whg:whg@192.168.12.101/whg'
    QUEUE = 'company_all'

    producer = ExampleProduct(URL, QUEUE)
    producer.run()
    # client = RabbitHelper(URL, QUEUE, True)
    # client.publish(json.dumps({
    #         'id': str(uuid.uuid1()),
    #         'swap_date': [2019, 1, 1],
    #         'data': f'测试！' * 100000
    #     }))

