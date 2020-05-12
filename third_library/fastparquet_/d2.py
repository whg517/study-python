# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d2
@Date: 2019/7/11 上午9:12
@Description:

"""

import pandas as pd
from fastparquet import write, ParquetFile
from hdfs.ext.kerberos import KerberosClient

client = KerberosClient('http://m1.node.hadoop:50070')

df = pd.DataFrame([
    {'id': '1', 'name': 'xxx', 'age': 12},
    {'id': '2', 'name': 'yyy', 'age': 13},
    {'id': '3', 'name': 'zzz', 'age': 10},
])


def open_write_write(filename, mode):
    return client.write(filename, overwrite=True)


def open_write_read(filename, mode):
    return client.read(filename)


def write_to_hdfs():
    write('/tmp/fastparquet/user1.parquet', df, open_with=open_write_write)


def read_from_hdfs():
    ParquetFile('/tmp/fastparquet/user1.parquet', open_with=open_write_read)


if __name__ == '__main__':
    """"""
    write_to_hdfs()
    # read_from_hdfs()
