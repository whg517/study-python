# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  demo
@Date: 2019/8/26 下午3:37
@Description:

"""

from twisted.web import server, resource
from twisted.internet import reactor, endpoints


class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, req):
        return b'<html>Hello, world !<html>'


site = server.Site(Simple())
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8888)
endpoint.listen(site)
reactor.run()
