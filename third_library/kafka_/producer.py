from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic


admin = KafkaAdminClient(bootstrap_servers='localhost')
admin.create_topics([NewTopic('test1', 3, 1)])

producer = KafkaProducer(
    bootstrap_servers='localhost'
)

producer.send(
    topic='test',
    key=b'test',
    value=b'test2'
)

producer.close()
