import asyncio
import time
from concurrent.futures import Future


def add(x, y, future: Future):
    res = x + y
    time.sleep(10)
    print(f'{x} + {y} = {res}')
    future.set_result(res)
    print(f'add method future done')


def sync_method():
    future = Future()
    global_loop.call_soon(add, 1, 2, future)
    while True:
        f'Waiting future done'
        if future.done():
            break
        else:
            print(f'Future result {future.result()}')
    print(f'sync_method done')


async def async_method():
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, sync_method)
    print(f'async_method done')


async def print_loop():
    print(f'print loop......\n')
    await asyncio.sleep(1)
    await asyncio.create_task(print_loop())


async def main():
    asyncio.create_task(print_loop())
    await async_method()


if __name__ == '__main__':
    global_loop = asyncio.get_event_loop()
    global_loop.create_task(main())
    global_loop.run_forever()
