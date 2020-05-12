from twisted.internet.defer import Deferred


def get_poem(res):
    print('Your poem is saved:')
    print(res)


def poem_failed(err):
    print(err.__class__)
    print(err)
    print('No poetry for yuou.')


d = Deferred()

d.addCallbacks(get_poem, poem_failed)

d.errback(Exception('I have failed.'))
