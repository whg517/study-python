import gzip
import json
import os
import sys
import time
from datetime import datetime
from functools import reduce
from typing import Dict

count = 0


def typeof(variate):
    if isinstance(variate, int):
        return 'int'
    elif isinstance(variate, bool):
        return 'boolean'
    elif isinstance(variate, str):
        return 'string'
    elif isinstance(variate, float):
        return 'flog'
    elif isinstance(variate, list):
        return 'list'
    elif isinstance(variate, dict):
        return 'dict'
    elif isinstance(variate, tuple):
        return 'tuple'
    elif isinstance(variate, set):
        return 'set'
    elif variate is None:
        return 'null'
    else:
        raise Exception(f'<{variate}> unknown type !')


def read(filename, skip=0):
    global count
    tmp = 0
    with gzip.open(filename=filename, mode='rb') as f:
        for line in f:
            count += 1
            tmp += 1
            if skip > tmp:
                continue
            yield json.loads(line, encoding='utf-8')


def log_count():
    global count
    print(f'\rRead line: {count}', end='', flush=True)


def list_path(path, suffix=''):
    path = path.rstrip('/')
    children = []
    for child in os.listdir(path):
        if child.startswith('.'):
            continue
        _path = f'{path}/{child}'
        if os.path.isdir(_path):
            children.extend(list_path(_path, suffix=suffix))
        else:
            if suffix:
                if _path.endswith(suffix):
                    children.append(_path)
            else:
                children.append(_path)
    return children


def collect_fields(lines):
    """"""
    fields = {}
    for line in lines:
        log_count()
        for key, value in line.items():
            value_type = typeof(value)
            if key in fields.keys():
                fields_value = fields.get(key)  # type: dict
                if value_type not in fields_value.keys():
                    fields_value.update({value_type: value})

            else:
                fields_value = {value_type: value}
            fields.update({key: fields_value})
    return fields


def write2file(path, data):
    paths = path.split('/')
    filename = f'{paths[-1].split(".")[0]}.json'

    path = '/'.join([fields_path] + paths[:-1])
    if not os.path.exists(path):
        os.makedirs(path)
    path = '/'.join([path, filename])
    with open(path, 'w') as file:
        if isinstance(data, str):
            file.write(data)
        else:
            data = json.dumps(data, indent=4, ensure_ascii=False)
            file.write(data)
        print(f'\rRead line: {count}')
        print(f'Write fields to {path}')
        print()


def migrate_fields(data1: Dict[str, Dict], data2: Dict[str, Dict]):
    """
    {
        "a": {
            "int": 1
        },
        "b": {
            "int": 2,
            "string": "a"
        }
    }
    :param data1:
    :param data2:
    :return:
    """
    for key, value in data2.items():
        if key in data1.keys():
            data1_value = data1.get(key)
            for k, v in value.items():
                if k not in data1_value.keys():
                    data1_value.update({k: v})
            data1.update({key: data1_value})
        else:
            data1.update({key: value})
    return data1


def migrate_all_fields():
    def read(file):
        with open(file, 'r', encoding='utf-8') as reader:
            return json.loads(reader.read())

    paths = list(set([os.path.join('/', *i.split('/')[:-1]) for i in list_path(fields_path)]))

    for path in paths:
        print(f'Migrate fields from <{path}>')
        migrated = reduce(migrate_fields, [read(os.path.join(path, i)) for i in os.listdir(path)])
        with open(f'{path}/migrate.json', 'w', encoding='utf-8') as writer:
            writer.write(json.dumps(migrated, indent=4, ensure_ascii=False))

    print(f'Migrate fields finish')


def run(path, suffix=''):
    print(datetime.now())
    start = time.perf_counter()
    for child in list_path(path, suffix):
        print()
        print(f'Collect field from file <{child}>')
        fields = collect_fields(read(child))
        write2file(child.replace(path, ''), fields)
    end = time.perf_counter()
    print()
    print(datetime.now())
    print(f'Time: {end - start}')
    print(f'Collect fields finish. Begin migrate fields...')
    migrate_all_fields()


def sorted_fields():
    """"""


def sorted_all_fields(root_path):
    def read(file):
        with open(file, 'r', encoding='utf-8') as reader:
            return json.loads(reader.read())

    paths = list(set([os.path.join('/', *i.split('/')[:-1]) for i in list_path(root_path)]))

    for path in paths:
        print(f'Migrate fields from <{path}>')
        for i in os.listdir(path):
            if i == 'migrate.json':
                data = read(os.path.join(path, i))
                data = {k: v for k, v in sorted(data.items())}
                with open(f'{path}/migrate_sorted.json', 'w', encoding='utf-8') as writer:
                    writer.write(json.dumps(data, indent=4, ensure_ascii=False))




def t():
    """"""
    root = '/data/customs/vietnam/imports/'
    vietnam = 'vietnam_201301-201312.json.gz'
    # res = run(f'{root}{vietnam}')

    lines = [
        {'a': 1, 'b': 2},
        {'a': 1, 'b': "a"},
        {'a': 1, 'b': True, 'c': [1, 2, 3]},
    ]

    res = collect_fields(lines)
    print(json.dumps(res, indent=4))
    print(f'Count: {count}')

    a = '/data/customs/vietnam/imports/vietnam_201401-201412.json.gz'.replace('/data/customs/', '')

    write2file(a, res)


if __name__ == '__main__':
    fields_path = '/tmp/customs'

    args = sys.argv[1:3]

    # run(*args)
    # run('/data/customs/')
    sorted_all_fields('/data/customs/customs')
