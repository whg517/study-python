# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d6
@Date: 2019/8/27 下午5:21
@Description:

"""

import logging

from twisted.internet import reactor
from twisted.web.resource import Resource, NoResource, IResource
from twisted.web.server import Site

from calendar import calendar

from zope.interface import implementer

logging.basicConfig(level=logging.DEBUG)


class YearPage(Resource):
    def __init__(self, year):
        Resource.__init__(self)
        self.year = year

    def render_GET(self, request):
        return f"<html><body><pre>{calendar(self.year)}</pre></body></html>".encode()


class CalendarHome(Resource):
    def getChild(self, name, request):
        if name == b'':
            return self

    def render_GET(self, request):
        return b"<html><body>Welcome to the calendar server!</body></html>"


class TestPage(IResource):

    def render_GET(self, req):
        return b'xx'


root = CalendarHome()
root.putChild(b'xx', TestPage())
factory = Site(root)
reactor.listenTCP(8000, factory)
reactor.run()
