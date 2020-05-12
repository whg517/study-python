import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()


def confirm_handler(frame):
    print(frame)


channel.confirm_delivery(callback=confirm_handler)

exchange = 'test_confirm'
queue = 'test_confirm'
message = 'xxx'
channel.exchange_declare(
    exchange=exchange,
    exchange_type='direct',
    passive=False,
    durable=False,
    auto_delete=False,
    internal=False,
    arguments=None
)

channel.queue_declare(
    queue=queue,
    passive=False,
    durable=False,
    exclusive=False,
    auto_delete=False,
    arguments=None
)

# channel.basic_publish(
#     exchange,
#     routing_key=,
#     body=message,
#     properties=None,
#     mandatory=False
# )


connection.close()
