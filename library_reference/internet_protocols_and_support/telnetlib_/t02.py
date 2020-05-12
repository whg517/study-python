# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  t02
@Date: 2018/12/18 9:46
@Description:
"""
import socket

__author__ = 'wanghuagang'


def interact(host, port):
    from telnetlib import Telnet

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((host, port))
    s.listen(5)
    cli = s.accept()[0]
    s.close()
    print("[+] Got connect-back")

    t = Telnet()
    t.sock = cli
    t.interact()


if __name__ == "__main__":
    """"""
    h = '127.0.0.1'
    p = 8889
    interact(h, p)
