# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d1
@Date: 2019/7/15 上午10:27
@Description:

"""

from hdfs.ext.kerberos import KerberosClient

client = KerberosClient('http://m1.node.hadoop:50070')

with client.read('/tmp/fastparquet/user1.parquet') as reader:
    features = reader.read()
    print(features)
