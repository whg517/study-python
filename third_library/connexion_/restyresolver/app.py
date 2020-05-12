# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  app
@Date: 2018/12/13 17:56
@Description:
"""

__author__ = 'wanghuagang'

import logging

import connexion
from connexion.resolver import RestyResolver

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    app = connexion.FlaskApp(__name__)
    app.add_api('resty-api.yaml',
                arguments={'title': 'RestyResolver Example',
                           "swagger_ui": True},
                resolver=RestyResolver('api'))
    app.run(port=9090)
