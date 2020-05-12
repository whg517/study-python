# encoding: utf-8

"""

@author: wanghuagang

@contact: kiven517@126.com

@software: 

@site: 

@file: t.py

@time: 2018/8/10 17:10

@desc:

"""

__author__ = 'wanghuagang'

import csv

"""
Dialect.delimiter
用于分隔字段的单字符字符串。它默认为','。

Dialect.quotechar
一个单字符的字符串，用于引用包含特殊字符的字段，例如分隔符或quotechar，或者包含换行符。它默认为'"'。

"""

# with open('eggs.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))


# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

data = {'aa': 111,
        'b.,b/': 222,
        'cc': 333,
        'dd': 444,
        'ee': 555,
        'ff': 666,
        'gg': 777}

with open('eggs.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerows([[key, value] for key, value in data.items()])

with open('eggs.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
