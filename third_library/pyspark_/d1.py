# encoding: utf-8

"""
@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d1
@Date: 2019/4/19 10:48
@Description:
"""
import logging

from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('').setMaster('local')
sc = SparkContext(conf=conf)

sc.setLogLevel('DEBUG')

rdd = sc.textFile('hdfs://192.168.10.1:8020/user/whg/test/yarn-site.xml')
print(rdd.collect())
