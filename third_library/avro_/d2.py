import avro
from avro.datafile import DataFileWriter
from avro.io import DatumWriter
from hdfs.ext.avro import AvroWriter

schema = {
    "namespace": "example.avro",
    "type": "record",
    "name": "Log",
    "fields": [
        {"name": "ip", "type": "string"},
        {"name": "additional", "type": {"type": "map", "values": "string"}}
    ]
}

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
            "microseconds": '223',
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

schema = avro.schema.SchemaFromJSONData(schema)

writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
for i in records:
    writer.append(i)
writer.close()

# from hdfs.ext.kerberos import KerberosClient
#
# client = KerberosClient('http://m1.node.hadoop:50070')
#
# with AvroWriter(client, '/tmp/hdfscli_avro/a.avro', overwrite=True) as writer:
#     for record in records:
#         writer.write(record)
