import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
#
# message = ' '.join(sys.argv[2:]) or 'Hello World!'

routing_key = 'kern.'
message = 'kernabc'

channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)

print(f'[x] Sent: {routing_key}, {message}')
