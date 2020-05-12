import json
import gzip
import logging
import os
import signal
import sys
import traceback
import uuid
import datetime
import avro
from avro.datafile import DataFileWriter
from avro.io import DatumWriter, AvroTypeException
from bson import ObjectId
from hdfs.ext.kerberos import KerberosClient

CHARACTER = 'utf-8'

SIGNAL_STOP = False

LOG_LEVEL = 'INFO'
LOG_FILE = 'customs_mongo2hdfs.log'

logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL)

# FORMAT
formatter = logging.Formatter('%(levelname)s:%(asctime)s: %(message)s; %(filename)s:%(lineno)d')

# ConsoleHandle
console_handle = logging.StreamHandler()
console_handle.setFormatter(formatter)
console_handle.setLevel(logging.DEBUG)
logger.addHandler(console_handle)

# FileHandle
file_handler = logging.FileHandler(LOG_FILE)

file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)


# logger.addHandler(file_handler)


def signal_handler(sig, frame):
    global SIGNAL_STOP
    logger.warning('You pressed Ctrl+C! Save breakpoint data......')
    SIGNAL_STOP = True


client = KerberosClient('http://m1.node.hadoop:50070')


class Migrate(object):
    BREAKPOINT_FILENAME = 'breakpoint.txt'
    TIME_FORMAT = '%Y%m%d%H%M%S'

    def __init__(self, schema_file, source_path, dist_path):
        """
        TODO source path 可以扫描下面全部文件，配合扫描 schema 文件，自动插入
        :param schema_file:
        :param source_path:
        :param dist_path:
        """
        self.schema = avro.schema.Parse(open(schema_file, 'rb').read())
        self.source_path = source_path
        self.dist_path = dist_path
        self.save_count = 0
        self.records = []
        self.swap_time = ''

        self.per_file_item_num = 10000

    def read(self, filename, skip=0):
        tmp = 0
        with gzip.open(filename=filename, mode='rb') as f:
            for line in f:
                tmp += 1
                if skip > tmp:
                    continue
                yield json.loads(line, encoding='utf-8')

    def construct_data(self, data):
        for d in data:
            """"""
            date = d['date']['$date']
            date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f%z').date()
            if self.save_count == 0:
                self.swap_time = date

            if len(self.records) >= self.per_file_item_num:
                yield self.swap_time, self.records

                self.records.clear()

            if self.swap_time != date:
                yield self.swap_time, self.records

                self.swap_time = date
                self.records.clear()

            self.records.append(d)

        yield self.swap_time, self.records

    def construct_path(self, date: datetime.date, compress):

        year = date.year
        month = date.month
        day = date.day
        _id = uuid.uuid1()

        filename_suffix = '.avro'
        if compress == 'snappy':
            filename_suffix = f'.{compress}{filename_suffix}'

        file_path = os.path.join(self.dist_path, f'year={year}', f'month={month}', f'day={day}')
        file_name = f'{year}{month}{day}-{_id}{filename_suffix}'
        return os.path.join(file_path, file_name)

    def write(self, filename, records):
        if filename.split('.')[-2] == 'snappy':
            compress = 'snappy'
        else:
            compress = 'null'
        try:
            with client.write(filename, overwrite=True) as writer:
                with DataFileWriter(writer, DatumWriter(), self.schema, codec=compress) as data_file_writer:
                    for record in records:
                        self.exit()
                        _id = record['_id']['$oid']
                        etl(record)

                        self.log_count()

                        data_file_writer.append(record)
                        self.save_count += 1
        except AttributeError as e:
            logger.error(f'record: {_id}')

            logger.info(json.dumps(record, indent=4, ensure_ascii=False))
            traceback.print_exc()
            # raise e
        except AvroTypeException as e:
            logger.info(f'Save Count: {self.save_count}')
            logger.error(f'record: {_id}')
            logger.info(json.dumps(record, indent=4, ensure_ascii=False))
            raise e

    def exit(self):
        if SIGNAL_STOP:
            logger.info(f'Save data count: {self.save_count}')
            logger.info(f'{datetime.datetime.now()} Exiting!')
            sys.exit(0)

    def log_count(self):
        if not self.save_count % 10000:
            logger.info(f'{datetime.datetime.now()} Saved data count: {self.save_count}')

    def save_breakpoint(self):
        with open(self.BREAKPOINT_FILENAME, 'w', encoding='utf-8') as writer:
            writer.write(f'{datetime.datetime.now().strftime(self.TIME_FORMAT)} {self.save_count}')

        logger.info(f'Saved breakpoint to file: {self.BREAKPOINT_FILENAME}')

    def parse_breakpoint(self):
        if os.path.isfile(self.BREAKPOINT_FILENAME):
            with open(self.BREAKPOINT_FILENAME, 'r', encoding='utf-8') as reader:
                line = reader.read()
                return int(line.split(' ')[1])
        else:
            return 0

    def run(self, skip=0, compress=''):
        """"""
        for date, data in self.construct_data(self.read(self.source_path, skip=skip)):
            self.write(self.construct_path(date, compress), data)


def exec_keys(method, data, keys):
    return all([method(data, key) for key in keys])


def etl(data: dict):
    """"""
    if isinstance(data['cif'], dict):
        data.update({'cif': int(data['cif']['$numberLong'])})


def get_example(filename, count=2):
    tmp = 0
    with gzip.open(filename=f'{path}/{filename}', mode='rb') as f:
        for line in f:
            tmp += 1
            res = json.dumps(json.loads(line.decode(CHARACTER)), indent=4, ensure_ascii=False)
            print(res)
            if tmp >= 2:
                break


if __name__ == '__main__':
    """"""
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    path = '/data/customs/vietnam/imports/'
    vietnam = 'vietnam_201301-201312.json.gz'
    north_america = 'north_america_200601-200612.json.gz'
    schema_file = 'schemas/customs/imports_vietnam.avsc'

    # get_example(north_america)

    migrate = Migrate(schema_file, f'{path}/{vietnam}', '/tmp/customs/vietnam/')
    migrate.run()
    # migrate.run(skip=7199+4666+1+54776+1+18485)
