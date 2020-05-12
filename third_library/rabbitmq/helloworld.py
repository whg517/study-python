# encoding: utf-8

"""
@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  helloworld
@Date: 2019/5/14 11:23
@Description:
"""
import json
import sys
import threading
from datetime import datetime

import pika

URL = 'amqp://whg:whg@192.168.12.101/whg'
QUEUE = 'company_all'


def send(length=1):
    data = {
        'id': 1,
        'name': 'xxx',
    }
    with pika.BlockingConnection(pika.URLParameters(URL)) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=QUEUE, durable=True)
        for l in range(length):
            swap_date = datetime.now()
            data.update({'swap_date': [swap_date.year, swap_date.month, swap_date.day]})
            body = json.dumps(data)
            channel.basic_publish(exchange='',
                                  routing_key=QUEUE,
                                  body=body)
            print(body)


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


if __name__ == '__main__':
    """"""
    # args = sys.argv[1:]
    # if args[0] == 'send':
    #     send()
    # elif args[0] == 'receive':
    #     receive()
    send(48)
    # receive()
