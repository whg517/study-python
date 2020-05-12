# encoding: utf-8

"""

@author: wanghuagang

@contact: kiven517@126.com

@software: 

@site: 

@file: t2.py

@time: 2018/8/23 10:54

@desc:

"""

import random
import functools

__author__ = 'wanghuagang'


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'decorator!')
        return func(*args, **kwargs)

    return wrapper


def debug(func):
    """Print the function signature and return value"""

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]  # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)  # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")  # 4
        return value

    return wrapper_debug


@debug
def p(i):
    print(i)
    return i


PLUGINS = dict()


def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f"Hello {name}"


@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)


def run():
    pass


if __name__ == '__main__':
    pass
