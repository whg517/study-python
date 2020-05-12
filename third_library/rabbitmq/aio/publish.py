import asyncio
import logging
from asyncio.unix_events import _UnixSelectorEventLoop

import pika
from pika.adapters.asyncio_connection import AsyncioConnection


class Publish:

    def __init__(self, amqp_url):
        self.amqp_url = amqp_url

        self.exchange = 'test'
        self.queue = 'test'
        self._connection = None
        self._channel = None
        self._publish_fut = asyncio.get_event_loop().create_future()

    def connect(self):
        return AsyncioConnection(
            on_open_callback=self.on_connect_open,
        )

    def on_connect_open(self, _unused_connection):
        self._connection.channel(on_open_callback=self.on_channel_open)

    def on_channel_open(self, channel):
        self._channel = channel
        self._channel.exchange_declare(
            exchange=self.exchange,
            exchange_type='direct',
            callback=self.on_queue_declared
        )

    def on_queue_declared(self, _unused_frame):
        self._channel.queue_declare(
            queue=self.queue,
            callback=self.on_queue_bind
        )

    def on_queue_bind(self, _unused_frame):
        self._channel.queue_bind(
            queue=self.queue,
            exchange=self.exchange,
            routing_key='#',
            arguments=None,
            callback=self.on_queue_bind_ok
        )

    def on_queue_bind_ok(self, _unused_frame):
        self._channel.confirm_delivery(
            ack_nack_callback=self.on_delivery_confirmation,
            callback=None
        )
        self._connection.ioloop.call_later(2, self.publish)
        self._connection.ioloop.call_later(4, self.publish)

    def on_delivery_confirmation(self, method_frame):
        print(method_frame.method.delivery_tag)
        print(method_frame)

    def publish(self):
        self._channel.basic_publish(
            exchange=self.exchange,
            routing_key='#',
            body='xxx',
            properties=None,
            mandatory=False
        )

    def run(self):
        self._connection = self.connect()
        loop = asyncio.get_event_loop()
        loop.run_forever()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    public = Publish('')
    public.run()
