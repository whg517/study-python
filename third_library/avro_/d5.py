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
              {
                  "name": "favorite_number",
                  "type": {
                      "type": "record",
                      "name": 'favorite_number',
                      "fields": [
                          {"name": "aa", "type": "string"}
                      ]
                  }
              },
          ]}

schema = avro.schema.SchemaFromJSONData(schema)

writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema, 'snappy')
writer.append({"name": "Alyssa", "favorite_number": {"aa": "a"}})

writer.close()

# reader = DataFileReader(open("users.avro", "rb"), DatumReader(reader_schema=schema))
# for line in reader:
#     print(line)
# reader.close()
