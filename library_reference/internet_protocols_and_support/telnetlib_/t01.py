# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  t01
@Date: 2018/12/17 16:19
@Description:
"""

__author__ = 'wanghuagang'

import telnetlib

t = telnetlib.Telnet()
t.open('localhost', 8889)

expect = ((r'Horizons>', 'DES=C/2012 X1\n'),
          (r'Continue.*:', 'y\n'),
          (r'Select.*E.phemeris.*:', 'E\n'),
          (r'Observe.*:', 'o\n'),
          (r'Coordinate center.*:', 'H06\n'),
          (r'Confirm selected station.*>', 'y\n'),
          (r'Accept default output.*:', 'y\n'),
          (r'Starting *UT.* :', '2013-Nov-7 09:00\n'),
          (r'Ending *UT.* :', '2013-Nov-17 09:00\n'),
          (r'Output interval.*:', '1d\n'),
          (r'Select table quant.* :', '1,4,9,19,20,24\n'),
          (r'Scroll . Page: .*%', ' '),
          (r'Select\.\.\. .A.gain.* :', 'X\n')
          )


while True:
    try:
        answer = t.expect(list(i[0] for i in expect), 10)
    except EOFError:
        break
    t.write(expect[answer[0]][1])
