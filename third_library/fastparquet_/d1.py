# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d1
@Date: 2019/6/28 下午2:16
@Description:

"""
import pandas as pd
from fastparquet import ParquetFile

parquet_file = 'shunqiwang.parquet'
pf = ParquetFile(parquet_file)
df = pf.to_pandas()  # type: pd.DataFrame

print(df.head(3))
