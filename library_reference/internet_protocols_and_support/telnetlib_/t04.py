# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  t04
@Date: 2019/1/18 10:02
@Description:
"""
import socket
import telnetlib

__author__ = 'wanghuagang'

host = '127.0.0.1'
port = 6023


def run():
    tn = telnetlib.Telnet(host, port)
    print(tn.read_until(b'\x1bc>>> \x1b[4h'))
    # # print(tn.read_very_lazy())
    tn.write(b'est()\n\n')
    # recv = tn.read_until(b'\r\r\r\n>>> \r\r\r\n>>> ')
    recv = tn.sock.recv(500)
    print(recv)
    tn.sock.close()


def t():
    with socket.create_connection((host, port)) as s:
        rec = s.recv(500)
        s.sendall(b'est()\n')
        print(rec)
        rec = s.recv(500)
        print(rec)
        s.close()


if __name__ == '__main__':
    run()
