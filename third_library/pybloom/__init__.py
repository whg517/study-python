# encoding: utf-8

"""

@Author: wanghuagang
@Contact: huagang517@126.com
@Project: StudyPython
@File:  __init__.py
@Date: 2019/7/2 下午3:48
@Description:

"""

import pybloom_live

import random, string


def _get_random_str(length=8):
    src_digits = string.digits  # string_数字
    src_lowercase = string.ascii_lowercase  # string_大写字母
    src_uppercase = string.ascii_uppercase  # string_小写字母

    # 随机生成数字大小写字母组成的个数

    if length > 9:
        length_random_max = 10
    else:
        length_random_max = random.randint(0, length - 1)
    digits_num = random.randint(1, length_random_max)
    uppercase_num = random.randint(1, length - digits_num - 1)
    lowercase_num = length - (digits_num + uppercase_num)
    # 生成字符串
    password = random.sample(src_digits, digits_num) + random.sample(src_uppercase, uppercase_num) + random.sample(
        src_lowercase, lowercase_num)
    # 打乱字符串
    random.shuffle(password)
    # 列表转换为字符串
    # return ''.join(password)
    return password


def get_random_str(length=8):
    random_str = []
    if length > 26:
        length = length - 26
        random_str.extend(_get_random_str(26))
        random_str.extend(get_random_str(length))
    else:
        random_str.extend(_get_random_str(length))

    return ''.join(random_str)


count = 0


def bloom():
    global count
    filter = pybloom_live.ScalableBloomFilter(mode=pybloom_live.ScalableBloomFilter.SMALL_SET_GROWTH)
    for i in range(10000000):
        count += 1
        try:
            url = get_random_str(random.randint(100, 500))
        except Exception:
            count -= 1
            continue

        if count % 100000 == 0:
            print(f'count: {count}')
        filter.add(url)

    with open('a.bloom', 'wb+') as f:
        filter.tofile(f)


if __name__ == '__main__':
    # bloom()
    # print(count)
    with open('a.bloom', 'rb') as f:
        filter = pybloom_live.ScalableBloomFilter.fromfile(f)
    pass
