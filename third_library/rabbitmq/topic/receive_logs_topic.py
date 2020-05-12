import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

# bind_keys = sys.argv[1:]
#
# if not bind_keys:
#     sys.stderr.write(f'Usage: {sys.argv[0]} [binding_key]...\n')
#     sys.exit(1)
#
# for bind_key in bind_keys:
#     channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=bind_key)

channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key='#')

print(f'[*] Waiting for logs. To exit pass CTRL+C')


def callback(ch, method, properties, body):
    print(f'[x] {method.routing_key}, {body}')


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
