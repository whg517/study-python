import json

from kafka.admin import NewTopic

from third_library.kafka_.utils import format_decorator


@format_decorator
def test_create_topic(client):
    topic = NewTopic('topic_1', 3, 1)
    response = client.create_topics([topic])
    # response =
    # CreateTopicsResponse_v3(throttle_time_ms=0, topic_errors=[(topic='test', error_code=0, error_message=None)])
    print(response)


@format_decorator
def test_list_topics(client):
    response = client.list_topics()
    print(response)


@format_decorator
def test_delete_topic(client):
    """
    :param client:
    :return:
    """
    response = client.delete_topics(
        [ 'topic-spider-APPID-8-8-24-20', '__consumer_offsets', 'topic-spider-APPID-7-7-23-19', 'topic-log',
         'topic-spider-APPID-7-7-21-17', 'topic-metric', 'topic-spider-APPID-9-9-25-21', 'topic-spider-APPID-7-7-22-18']
    )
    # response = DeleteTopicsResponse_v3(throttle_time_ms=0, topic_error_codes=[(topic='test', error_code=0)])
    print(response)


@format_decorator
def test_describe_topics(client):
    response = client.describe_topics(['test-1'])
    print(json.dumps(response, indent=4))


@format_decorator
def test_list_consumer_groups(client):
    response = client.list_consumer_groups()
    print(response)


@format_decorator
def test_describe_consumer_groups(client):
    response = client.describe_consumer_groups(['test'])
    print(response)


@format_decorator
def test_list_consumer_group_offsets(client):
    group_name = 'test'
    response = client.list_consumer_group_offsets(group_name)
    for topic_partition, offset_metadata in response.items():
        print(
            f'group: {group_name},',
            f'topic: {topic_partition.topic},',
            f'partition: {topic_partition.partition},',
            f'offset: {offset_metadata.offset},',
            f'metadata: {offset_metadata.metadata}'
        )
