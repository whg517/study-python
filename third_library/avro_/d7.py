import avro
import fastavro
from avro.datafile import DataFileWriter, DataFileReader
from avro.io import DatumWriter, DatumReader
from hdfs.ext.avro import AvroWriter

from hdfs.ext.kerberos import KerberosClient

client = KerberosClient('http://m1.node.hadoop:50070')

schema = {
    "namespace": "example.avro",
    "type": "record",
    "name": "Log",
    "fields": [
        {"name": "ip", "type": "string"},
        {"name": "additional", "type": {"type": "map", "values": "string"}},
        {"name": "loglevel", "type": "string", "default": "INFO"}

    ]
}

avro_schema = avro.schema.SchemaFromJSONData(schema)

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


def write():
    with DataFileWriter(open("users.avro", "wb"), DatumWriter(), avro_schema) as w:
        for i in records:
            w.append(i)


def read():
    with DataFileReader(open("users.avro", "rb"), DatumReader(reader_schema=avro_schema)) as r:
        for line in r:
            print(line)


def fast_avro_read():
    with open('users.avro', 'rb') as fo:
        avro_reader = fastavro.reader(fo, reader_schema=schema)
        for record in avro_reader:
            print(record)


if __name__ == '__main__':
    """"""
    fast_avro_read()
