# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d4
@Date: 2019/8/26 下午6:12
@Description:

"""

from twisted.application import internet, service
from twisted.internet import reactor
from twisted.web import static, server

root = static.File("/var/www/htdocs")
application = service.Application('web')
site = server.Site(root)
sc = service.IServiceCollection(application)
i = internet.TCPServer(8080, site)
i.setServiceParent(sc)
reactor.run()
