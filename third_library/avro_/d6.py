import avro
from avro.datafile import DataFileWriter, DataFileReader
from avro.io import DatumWriter
from hdfs.ext.avro import AvroWriter, AvroReader

from hdfs.ext.kerberos import KerberosClient

client = KerberosClient('http://m1.node.hadoop:50070')

schema = {
    "namespace": "example.avro",
    "type": "record",
    "name": "Log",
    "fields": [
        {"name": "ip", "type": "string"},
        {"name": "additional", "type": {"type": "map", "values": "string"}},
    ]
}

# schema = avro.schema.SchemaFromJSONData(schema)

records = [
    {
        "ip": "172.18.80.109",

        "additional": {
            "timestamp": "2015-09-17T23:00:18.313Z",
            "message": "blahblahblah",
        }
    },
    {
        "ip": "172.18.80.112",
        "additional": {
            "microseconds": "223",
        }
    },
    {
        "ip": "172.18.80.113",
        "additional": {
            "timestamp": "2015-09-17T23:00:08.299Z",
            "message": "blahblahblah",
            "thread": "http-apr-8080-exec-1147",
        }
    }
]


def read():
    """"""
    with AvroReader(client, '/tmp/hdfscli_avro/example.avro') as reader:
        for record in reader:
            print(record)


def write():
    with AvroWriter(client, '/tmp/hdfscli_avro/example.avro', overwrite=True, schema=schema) as writer:
        for record in records:
            writer.write(record)


if __name__ == '__main__':
    """"""
    read()
