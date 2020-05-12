# encoding: utf-8

"""

@author: wanghuagang

@contact: kiven517@126.com

@software: 

@site: 

@file: t1.py

@time: 2018/8/16 16:27

@desc:

"""

__author__ = 'wanghuagang'


def d(func):
    def _wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        print(d.__name__)
        return f
        pass

    return _wrapper


def c(func):
    def _wrapper(*args, **kwargs):
        # f = func(*args, **kwargs)
        # print(c.__name__)
        # return f
        pass

    return _wrapper


@d
@c
def p(a):
    print(a)


if __name__ == "__main__":
    p(1)
    pass
