# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d1
@Date: 2019/8/9 下午4:53
@Description:

"""
import pytest
from elasticsearch import Elasticsearch


def search(es: Elasticsearch, index):
    res = es.search(index=index)
    return res


def test_search(mocker):
    """"""
    es = mocker.Mock()
    mocker.spy(es, 'search')
    search(es, 'test')
    es.search.assert_called_with(index='test')
