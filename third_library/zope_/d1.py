# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  d1
@Date: 2019/8/16 上午10:55
@Description:

"""
import zope
import zope.interface

from zope.interface import implementer, provider


# 定义接口
class IFoo(zope.interface.Interface):
    """Foo blah blah"""
    x = zope.interface.Attribute("""X blah blah""")

    def bar(q, r=None):
        """bar blah blah"""


"""
提供：对象提供接口。如果对象提供接口，则接口指定对象的行为。即接口指定提供他们对象的行为
实现：类实现接口。如果类实现接口，则类的实例提供接口。对象提供了其类实现的接口。（除了类实现对象外，对象也可以直接提供接口。）

类通常不提供他们实现的接口

如果使用工厂方式，对于任何可调用对象，可以通过声明工厂实现接口来声明它生成提供某些接口的对象
"""


# 声明实现的接口
@implementer(IFoo)
class Foo(object):
    # zope.interface.implements(IFoo)

    def __init__(self, x=None):
        self.x = x

    def bar(self, q, r=None):
        return q, r, self.x

    def __repr__(self):
        return f'Foo({self.x})'


"""
# 接口是否被类实现？
IFoo.implementedBy(Foo)
Out[3]: True
"""

"""
# 实现接口的类的对象是否提供接口？    (如果类实现接口，则类的实例提供接口，对象提供了其类实现的接口)
foo = Foo()
IFoo.providedBy(foo)
Out[5]: True
"""

"""
# 实现接口的类是否提供接口？   (如果类实现接口，则类的实例提供接口。类通常不提供他们实现的接口)
IFoo.providedBy(Foo)
Out[6]: False
"""

"""
# 查看类实现了哪些接口？
list(zope.interface.implementedBy(Foo))
Out[7]: [<InterfaceClass __main__.IFoo>]
"""

"""
# 查看对象提供哪些接口？
list(zope.interface.providedBy(foo))
Out[8]: [<InterfaceClass __main__.IFoo>]
"""


def y_foo(y):
    foo = Foo()
    foo.y = y
    return foo


"""
# 对于任何可调用对象，可以通过声明工厂实现接口来声明它生成提供某些接口的对象
y_foo = zope.interface.implementer(IFoo)(y_foo)
list(zope.interface.implementedBy(y_foo))
Out[4]: [<InterfaceClass __main__.IFoo>]
"""


class YFactory(object):
    def __call__(self, y):
        foo = Foo()
        foo.y = y
        return foo


"""
y_foo = YFactory()
y_foo = zope.interface.implementer(IFoo)(y_foo)
list(zope.interface.implementedBy(y_foo))
Out[5]: [<InterfaceClass __main__.IFoo>]
"""


# 声明提供的接口
class IFooFactory(zope.interface.Interface):
    def __call__(x=None):
        """Create a foo
        The argument provides the initial value for x ...
        """


"""
# 类通常不提供他们实现的接口
# 如果使用工厂方式，对于任何可调用对象，可以通过声明工厂实现接口来声明它生成提供某些接口的对象
zope.interface.directlyProvides(Foo, IFooFactory)
list(zope.interface.providedBy(Foo))
Out[7]: [<InterfaceClass __main__.IFooFactory>]
IFooFactory.providedBy(Foo)
Out[8]: True
"""


@implementer(IFoo)
@provider(IFooFactory)
class Foo2(object):
    def __init__(self, x=None):
        self.x = x

    def bar(self, q, r=None):
        return q, r, self.x

    def __repr__(self):
        return f'Foo({self.x})'


"""
# 声明类接口很常见
list(zope.interface.providedBy(Foo2))
Out[3]: [<InterfaceClass __main__.IFooFactory>]
"""


# ###########################################
# 有时候我们希望在实例上声明接口，即是这些实例从其类中获取接口
class ISpecial(zope.interface.Interface):
    reason = zope.interface.Attribute("Reason why we're special")

    def brag():
        """Brag about begin special"""


"""

foo = Foo()
foo.reason = 'I just am'
def brag():
    return "I'm special!"
foo.brag = brag
foo.reason
Out[8]: 'I just am'
foo.brag()
Out[9]: "I'm special!"
zope.interface.directlyProvides(foo, ISpecial)
ISpecial.providedBy(foo)
Out[11]: True
list(zope.interface.providedBy(foo))
Out[12]: [<InterfaceClass __main__.ISpecial>, <InterfaceClass __main__.IFoo>]
"""

"""
# 查看对象直接提供的接口
list(zope.interface.directlyProvidedBy(foo))
Out[13]: [<InterfaceClass __main__.ISpecial>]
newfoo = Foo()
list(zope.interface.directlyProvidedBy(newfoo))
Out[15]: []
"""