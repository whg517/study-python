# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d2
@Date: 2019/8/26 下午3:56
@Description:

"""
from twisted.internet import reactor
from twisted.web import server
from twisted.web.resource import Resource


class Hello(Resource):
    isLeaf = True

    def getChild(self, path, request):
        if path == '':
            return self
        return Resource.getChild(self, path, request)

    def render_GET(self, req):
        return f'Helloworld! I am located at {req.path},'.encode('utf-8')


resource = Hello()

site = server.Site(resource)
reactor.listenTCP(8080, site)
reactor.run()
