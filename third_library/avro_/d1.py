import logging
from datetime import datetime
import avro
import hdfs
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

from hdfs.ext.avro import AvroWriter, AvroReader

tmp_file = '/tmp/whg/20190617172619-00c2e005-2c3d-45bb-bdd5-03ff37147e42.avro'

schema = {"namespace": "example.avro",
          "type": "record",
          "name": "User",
          "fields": [
              {"name": "name", "type": "string"},
              {"name": "favorite_number", "type": ["int", "null"]},
              {"name": "favorite_color", "type": ["string", "null"]}
          ]}

schema = avro.schema.SchemaFromJSONData(schema)

# writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
# writer.append({"name": "Alyssa", "favorite_number": 256})
# writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
# writer.append({"name": "Alyssa", "favorite_number": 256})
# writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
# writer.append({"name": "Alyssa", "favorite_number": 256})
# writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
# writer.append({"name": "Alyssa", "favorite_number": 256})
# writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
# writer.close()

# reader = DataFileReader(open("users.avro", "rb"), DatumReader(reader_schema=schema))
# for line in reader:
#     print(line)
# reader.close()


from hdfs.ext.kerberos import KerberosClient

client = KerberosClient('http://m1.node.hadoop:50070')
#
# # print(client.list(''))
#
path = f'/tmp/test_avro/data-{datetime.now().timestamp()}.avro'

records = [
    {'name': 'xiaoming', 'favorite_number': 123, 'favorite_color': 'red'},
    {'name': 'xiaohong', 'favorite_number': 123, 'favorite_color': 'yellow'},
    {'name': 'xiaoliang', 'favorite_number': 123, 'favorite_color': 'black'}
]
#
# with client.write(path, overwrite=True) as writer:
# #     for record in records:
# #         writer.write(record)
#     with DataFileWriter(writer, DatumWriter(), schema) as data_file_writer:
#         for record in records:
#             data_file_writer.append(record)


with AvroWriter(client, path) as writer:
    for record in records:
        writer.write(record)
#
# with AvroReader(client, '/tmp/test_avro/data-1560762234.783534.avro') as reader:
#     schema = reader.schema  # The remote file's Avro schema.
#     print(schema)
#     content = reader.content  # Content metadata (e.g. size).
#     for record in reader:
#         print(record)
