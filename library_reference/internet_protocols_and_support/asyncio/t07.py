import asyncio


async def task_a():
    print('A')
    result = await task_a_a()


async def task_b():
    print('task_b')
    await task_a_b()


async def task_c():
    print('C')
    result = await task_c_b()


# ========================

async def task_a_a():
    await asyncio.sleep(2)
    return 'task_a_a'


async def task_a_b():
    return task_a_b


async def task_a_c():
    return task_a_c


async def task_b_a():
    return task_b_a


async def task_b_b():
    return task_b_b


async def task_c_a():
    print('task_c_a')


async def task_c_b():
    print('C B')
    await asyncio.sleep(1)
    await task_c_b_a()


# ========================

async def task_c_b_a():
    print('C B A')
    await asyncio.sleep(1)
    return 'task_c_b_a'


def main(loop):
    print('main')
    loop.create_task(task_a())
    loop.create_task(task_c())
    loop.call_later(1, main, loop)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()

    event_loop.call_soon(main, event_loop)

    event_loop.run_forever()
