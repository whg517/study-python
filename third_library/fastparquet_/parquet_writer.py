# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  parquet_writer
@Date: 2019/7/11 上午9:23
@Description:

"""
import logging
import os
from json import dumps

import fastparquet
from fastparquet import ParquetFile
from fastparquet.util import metadata_from_many, default_open, join_path
from hdfs import HdfsError
from hdfs.ext.avro import _SchemaInferrer
from hdfs.util import AsyncWriter

_logger = logging.getLogger(__name__)
# The number of bytes in a sync marker (http://mtth.xyz/_9lc9t3hjtx69x54).
SYNC_SIZE = 16


class ParquetWriter(ParquetFile):

    def __init__(self, fn, verify=False, open_with=default_open,
                 root=False, sep=None):
        if isinstance(fn, (tuple, list)):
            basepath, fmd = metadata_from_many(fn, verify_schema=verify,
                                               open_with=open_with, root=root)
            if basepath:
                self.fn = join_path(basepath, '_metadata')  # effective file
            else:
                self.fn = '_metadata'
            self.fmd = fmd
            self._set_attrs()
        elif hasattr(fn, 'read'):
            # file-like
            self._parse_header(fn, verify)
            if self.file_scheme not in ['simple', 'empty']:
                raise ValueError('Cannot use file-like input '
                                 'with multi-file data')
            open_with = lambda *args, **kwargs: fn
            self.fn = None
        else:
            try:
                fn2 = join_path(fn, '_metadata')
                self.fn = fn2
                with open_with(fn2, 'rb') as f:
                    self._parse_header(f, verify)
                fn = fn2
            except (IOError, OSError):
                self.fn = join_path(fn)
                with open_with(fn, 'rb') as f:
                    self._parse_header(f, verify)
        self.open = open_with
        self.sep = sep
