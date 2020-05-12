import functools


def format_print(*args):
    print('\n=================')
    print(*args)
    print('==================\n')


def format_decorator(func: object) -> object:
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        print('\n==================\n')
        res = func(*args, **kwargs)
        print('\n==================\n')
        return res

    return _wrapper
