# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d1
@Date: 2019/7/11 上午9:41
@Description:

"""

import pyarrow.parquet as pq
import pandas as pd
import numpy as np
import pyarrow as pa

df = pd.DataFrame({'one': [-1, np.nan, 2.5],
                   'two': ['foo', 'bar', 'baz'],
                   'three': [True, False, True]},
                  index=list('abc'))

print(df.head())

table = pa.Table.from_pandas(df=df)

print(table.num_rows)
