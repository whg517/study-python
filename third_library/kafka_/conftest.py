import pytest
from kafka import KafkaProducer, KafkaAdminClient


@pytest.fixture
def client():
    c = KafkaAdminClient(bootstrap_servers='localhost')
    yield c
    c.close()


@pytest.fixture
def producer():
    p = KafkaProducer(
        bootstrap_servers='localhost'
    )
    yield p
    p.close()
