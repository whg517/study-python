# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  client
@Date: 2018/12/18 15:43
@Description:
"""

__author__ = 'wanghuagang'

import socket

HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    s.recvfrom()
    data = s.recv(1024)
    print(f'Received {repr(data)}')


"""

import socket

HOST = '127.0.0.1'
PORT = 6023
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
s.sendall(b'Hello, world')
"""