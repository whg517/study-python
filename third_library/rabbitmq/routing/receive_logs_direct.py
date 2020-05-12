import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(exchange='spiderkeeper.schedule.effect', exchange_type='direct')

result = channel.queue_declare(queue='spiderkeeper.environment.effect')

queue_name = result.method.queue

channel.queue_bind(exchange='spiderkeeper.schedule.effect', queue=queue_name, routing_key='error')


def callback(cn, method, properties, body):
    print(f'[x] {method.routing_key}, {body}')


channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)

channel.start_consuming()
