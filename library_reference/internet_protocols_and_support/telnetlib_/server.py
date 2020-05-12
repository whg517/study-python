# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  server
@Date: 2018/12/17 16:27
@Description:
"""

import socket

__author__ = 'wanghuagang'


def run():
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8889))
    sk.listen(5)

    conn, address = sk.accept()

    sk.sendall(bytes("Hello world", encoding="utf-8"))


if __name__ == '__main__':
    run()
