DROP TABLE IF EXISTS imports_vietnam;

CREATE EXTERNAL TABLE imports_vietnam
PARTITIONED BY (year int, month int, day int)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION '/tmp/customs/vietnam/'
TBLPROPERTIES ('avro.schema.literal'='{
    "name": "imports_vietnam",
    "type": "record",
    "namespace": "cn.tendata.customs.imports.dataset",
    "fields": [
        {"name":  "decNo", "type": ["string","null"]},
        {"name":  "exporterCode", "type": ["string","null"]},
        {"name":  "exporter", "type": ["string","null"]},
        {"name":  "exporterAddr", "type": ["string","null"]},
        {"name":  "exporterTel", "type": ["string","null"]},
        {"name":  "importer", "type": ["string","null"]},
        {"name":  "importerAddr", "type": ["string","null"]},
        {"name":  "importerCountry", "type": ["string","null"]},
        {"name":  "hsCode", "type": ["string","null"]},
        {"name":  "countryOfDestination", "type": ["string","null"]},
        {"name":  "portOfDeparture", "type": ["string","null"]},
        {"name":  "portOfArrival", "type": ["string","null"]},
        {"name":  "customsAgency", "type": ["string","null"]},
        {"name":  "incoterms", "type": ["string","null"]},
        {"name":  "invoiceCurrency", "type": ["string","null"]},
        {"name":  "payment", "type": ["string","null"]},
        {"name":  "currency", "type": ["string","null"]},
        {"name":  "qty", "type": ["double","null"]},
        {"name":  "qtyU", "type": ["string","null"]},
        {"name":  "fobU", "type": ["string","null"]},
        {"name":  "fob", "type": ["string","null"]},
        {"name":  "usFob", "type": ["string","null"]},
        {"name":  "tax", "type": ["double","null"]},
        {"name":  "taxRate", "type": ["string","null"]},
        {"name":  "taxCurrency", "type": ["string","null"]},
        {"name":  "transMode", "type": ["string","null"]},
        {"name":  "goodsDesc", "type": ["string","null"]},

        {"name":  "billNo", "type": ["string","null"]},
        {"name":  "importerId", "type": ["string","null"]},
        {"name":  "importerTel", "type": ["string","null"]},
        {"name":  "exporterCountry", "type": ["string","null"]},
        {"name":  "countryOfOrigin", "type": ["string","null"]},
        {"name":  "countryOfTrade", "type": ["string","null"]},
        {"name":  "transAgency", "type": ["string","null"]},
        {"name":  "vndU", "type": ["string","null"]},
        {"name":  "cifU", "type": ["double","null"]},
        {"name":  "cif", "type": ["double","null"]},
        {"name":  "usCif", "type": ["double","null"]}
    ]
}');