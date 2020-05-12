import json
import logging

import pytest
from kafka import KafkaAdminClient, KafkaProducer
from kafka.admin import NewTopic

# logging.basicConfig(level=logging.DEBUG)
from third_library.kafka_.utils import format_decorator


@format_decorator
def test_seed(producer):
    for i in range(1, 30):
        topic_name = 'topic_1'
        future = producer.send(topic_name, value=f'{topic_name}-{i}'.encode('utf-8'))
        record_metadata = future.get(timeout=5)
        print(
            record_metadata.topic,
            record_metadata.partition,
            record_metadata.offset
        )
