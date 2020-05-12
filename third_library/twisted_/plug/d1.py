from zope.interface import Interface, implementer
from twisted.python import components


class IAmericanSocket(Interface):

    def voltage(self):
        """

        :return:  return the voltage produced by this socket object, as an integer
        """


@implementer(IAmericanSocket)
class AmericanSocket:
    def voltage(self):
        return 120


class UKSocket:
    def voltage(self):
        return 240


@implementer(IAmericanSocket)
class AdaptToAmericanSocket:

    def __init__(self, original):
        """
        pass the original UKSocket object as original
        :param original:
        """
        self.original = original

    def voltage(self):
        return self.original.voltage() / 2


components.registerAdapter(
    AdaptToAmericanSocket,
    UKSocket,
    IAmericanSocket
)


class HairDryer:
    def plug(self, socket):
        adapted = IAmericanSocket(socket)
        assert adapted.voltage() == 120, 'BOOM'
        print('I was plugging in properly and am operating')
