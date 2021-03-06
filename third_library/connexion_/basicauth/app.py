# encoding: utf-8

"""
@Author: wanghuagang
@Contact: kiven517@126.com
@Project: StudyPython
@File:  app.py
@Date: 2018/12/13 17:37
@Description:
"""

__author__ = 'wanghuagang'

import connexion
from connexion.decorators.security import validate_scope
from connexion.exceptions import OAuthScopeProblem


def basic_auth(username, password, required_scopes=None):
    if username == 'admin' and password == 'secret':
        info = {'sub': 'admin', 'scope': 'secret'}
    elif username == 'foo' and password == 'bar':
        info = {'sub': 'user1', 'scope': ''}
    else:
        # optional: raise exception for custom error response
        return None

    # optional
    if required_scopes is not None and not validate_scope(required_scopes, info['scope']):
        raise OAuthScopeProblem(
            description='Provided user doesn\'t have the required access rights',
            required_scopes=required_scopes,
            token_scopes=info['scope']
        )

    return info


def dummy_func(token):
    return None


def get_secret(user) -> str:
    return "You are {user} and the secret is 'wbevuec'".format(user=user)


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__)
    app.add_api('openapi.yaml', arguments={"swagger_ui": True})
    app.run(port=8080)
