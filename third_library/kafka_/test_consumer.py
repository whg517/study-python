import time

import pytest
from kafka import KafkaConsumer, TopicPartition, OffsetAndMetadata
from kafka.consumer.subscription_state import SubscriptionState

from third_library.kafka_.utils import format_print, format_decorator


@pytest.fixture
def consumer():
    c = KafkaConsumer(
        group_id='group_1',
        bootstrap_servers='localhost'
    )
    yield c
    c.close()


@format_decorator
def test_seek_to_beginning(consumer):
    partition = TopicPartition('test', 2)
    consumer.assign([partition])
    consumer.seek_to_beginning(partition)
    response = consumer.position(partition)
    print(response)


@format_decorator
def test_poll(consumer):
    partition = TopicPartition('topic_1', 0)
    partition2 = TopicPartition('topic_2', 2)
    consumer.assign([partition, partition2])
    # consumer.seek_to_beginning(partition)
    # consumer.seek(partition, 3)
    msgs = consumer.poll(
        timeout_ms=1000,
        max_records=2,
        update_offsets=True
    )
    print(msgs)
    if msgs:
        for msg in msgs.get(partition):
            print("%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition,
                                                 msg.offset, msg.key,
                                                 msg.value))


@format_decorator
def test_seek_to_end(consumer):
    partition = TopicPartition('test', 2)
    consumer.assign([partition])
    response = consumer.seek_to_end(partition)
    print(response)


@format_decorator
def test_commit(consumer):
    partition = TopicPartition('test', 2)
    offset_metadata = OffsetAndMetadata(2, 'xx')
    response = consumer.commit({partition: offset_metadata})
    print(response)


@format_decorator
def test_position(consumer):
    partition = TopicPartition('test', 2)
    consumer.assign([partition])
    response = consumer.position(partition)
    print(response)


@format_decorator
def test_assignment(consumer):
    consumer.subscribe(topics=['topic_1'])
    print(consumer._coordinator.poll())
    result = consumer.assignment()
    print(result)


def test_partitions_for_topic(consumer):
    partitions = consumer.partitions_for_topic('topic_1')
    for partition in partitions:
        print(partition)


@format_decorator
def test_seek(consumer):
    partition = TopicPartition('test', 2)
    consumer.assign([partition])
    consumer.seek(partition, 3)


def unpack_msgs(msgs):
    if msgs:
        for topic, msg in msgs.items():
            print(f"Topic name: {topic.topic}")
            for m in msg:
                print("%s:%d:%d: key=%s value=%s" % (m.topic, m.partition,
                                                     m.offset, m.key,
                                                     m.value))


@format_decorator
def test_subscribe():
    consumer = KafkaConsumer(
        group_id='group_1',
        bootstrap_servers='localhost',
        auto_offset_reset='earliest',
        enable_auto_commit=False,
    )
    consumer.subscribe(topics=['topic_1'])
    # consumer.subscribe(pattern=r'topic.*')
    msgs = consumer.poll(
        timeout_ms=10 * 1000,
        max_records=2,
        update_offsets=False
    )
    print(msgs)
    unpack_msgs(msgs)
    consumer.commit()


@format_decorator
def test_topics(consumer):
    consumer.subscribe(topics=['topic_1'])
    topics = consumer.topics()
    print(topics)


@format_decorator
def test_sub_and_assign():
    consumer = KafkaConsumer(
        group_id='group_1',
        bootstrap_servers='localhost',
        auto_offset_reset='earliest',
        enable_auto_commit=False,
    )
    consumer.subscribe(topics=['topic_1'])
    consumer._coordinator.poll()
    consumer.
    # msgs = consumer.poll(
    #     timeout_ms=10 * 1000,
    #     max_records=2,
    #     update_offsets=False
    # )
    # unpack_msgs(msgs)
