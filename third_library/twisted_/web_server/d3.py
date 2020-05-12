# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d3
@Date: 2019/8/26 下午4:00
@Description:

"""
from twisted.web import server
from twisted.internet import reactor, endpoints
from twisted.web.resource import Resource


class Hello(Resource):
    # isLeaf = True

    def getChild(self, path, request):
        if path == '':
            return self
        return Resource.getChild(self, path, request)

    def render_GET(self, req):
        return f'Helloworld! I am located at {req.path}'.encode('utf-8')


class SubPage(Resource):
    isLeaf = True

    def render_GET(self, req):
        return b'Subpage'


root = Hello()
root.putChild(b'foo', SubPage())
root.putChild(b'bar', SubPage())

site = server.Site(root)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8081)
endpoint.listen(site)
reactor.run()
