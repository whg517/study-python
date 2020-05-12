import time

from kafka import KafkaConsumer, TopicPartition, OffsetAndMetadata, KafkaAdminClient
import traceback
from datetime import datetime


def consume_msg():
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                             message.offset, message.key,
                                             message.value))


def subscribe():
    consumer.subscribe(topics=['topic_1'])
    # consumer.subscribe(pattern=r'topic.*')
    count = 100
    while count > 0:
        count -= 1
        print(f'{datetime.now()} Poll data..')
        time.sleep(5)
        msgs = consumer.poll(
            timeout_ms=10,
            max_records=2,
            update_offsets=True
        )
        if msgs:
            for topic, msg in msgs.items():
                print(f"Topic name: {topic.topic}")
                for m in msg:
                    print("%s:%d:%d: key=%s value=%s" % (m.topic, m.partition,
                                                         m.offset, m.key,
                                                         m.value))


if __name__ == '__main__':
    admin = KafkaAdminClient(bootstrap_servers='localhost')
    consumer = KafkaConsumer(
        group_id='group_1',
        bootstrap_servers='localhost',
        auto_offset_reset='earliest',
        enable_auto_commit=False,
    )
    try:
        # partition = TopicPartition('test', 2)
        # consumer.assign([partition])
        # consumer.seek_to_beginning(partition)

        # consume_msg()
        subscribe()

    except Exception as e:
        traceback.print_exc(e)
    finally:
        consumer.close()
