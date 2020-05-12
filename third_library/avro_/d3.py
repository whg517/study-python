import avro
from avro.datafile import DataFileWriter, DataFileReader
from avro.io import DatumWriter

from hdfs.ext.kerberos import KerberosClient

client = KerberosClient('http://m1.node.hadoop:50070')

schema = {"namespace": "example.avro",
          "type": "record",
          "name": "User",
          "fields": [
              {"name": "name", "type": "string"},
              {"name": "favorite_number", "type": ["int", "null"]},
              {"name": "favorite_color", "type": ["string", "null"]}
          ]}

schema = avro.schema.SchemaFromJSONData(schema)

records = [
    {"name": "Alyssa", "favorite_number": 256},
    {"name": "Ben", "favorite_number": 7, "favorite_color": "red"}
]


def avro_writer(path):
    with client.write(path, overwrite=True) as writer:
        with DataFileWriter(writer, DatumWriter(), schema, codec='snappy') as avro_writer:
            for record in records:
                avro_writer.append(record)


# def avro_reader(path):
#     with client.read(path) as reader:
#         with DataFileReader(reader, DatumWriter()) as avro_reader:
#             for i in avro_reader:
#                 print(i)


if __name__ == '__main__':
    """"""
    avro_writer('/tmp/whg/user_favorite/001.snappy.avro')
