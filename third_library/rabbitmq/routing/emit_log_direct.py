import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

message = 'xxxxx'

channel.basic_publish(exchange='direct_logs', routing_key='error', body=message)

print(f'[x] Sent {message}')

connection.close()

connection.close()
