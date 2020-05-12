import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

# use default exchange
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='hello world!')

print('[x] Sent Hello world!')

connection.close()
