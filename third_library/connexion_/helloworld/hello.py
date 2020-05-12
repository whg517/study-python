# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  example
@Date: 2018/12/13 17:07
@Description:
"""

__author__ = 'wanghuagang'

import connexion


def post_greeting(name: str) -> str:
    return 'Hello {name}'.format(name=name)


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='openapi/')
    app.add_api('helloworld-api.yaml', arguments={'title': 'Hello World Example',
                                                  "swagger_ui": True})
    app.run()
