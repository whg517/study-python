DROP TABLE user_favorite;

CREATE EXTERNAL TABLE user_favorite
-- PARTITIONED BY (year int)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
LOCATION '/tmp/whg/user_favorite/'
TBLPROPERTIES ('avro.schema.literal'='{"namespace": "example.avro",
          "type": "record",
          "name": "User",
          "fields": [
              {"name": "name", "type": "string"},
              {"name": "favorite_number", "type": ["int", "null"]},
              {"name": "favorite_color", "type": ["string", "null"]}
          ]}');

SELECT * FROM user_favorite;

SHOW PARTITIONS user_favorite;

SHOW TBLPROPERTIES user_favorite;

MSCK REPAIR TABLE user_favorite;

ALTER TABLE user_favorite SET TBLPROPERTIES ("discover.partitions"="true");

INSERT INTO TABLE user_favorite
(name, favorite_number, year)
VALUES
('test', 20, 2019),
('test1', 11,2019);

INSERT INTO TABLE user_favorite
(name, favorite_color, year)
VALUES
('tes2', 'RED', 2019),
('test3', 'YELLOW', 2019);

INSERT INTO TABLE user_favorite
(name, favorite_color, year)
VALUES
('tes2', 'RED', 2018),
('test3', 'YELLOW', 2018);



SELECT * FROM user_favorite;

INSERT INTO TABLE user_favorite
(name, year)
VALUES
('test10', 2019);

SELECT * FROM test_code_partition;
