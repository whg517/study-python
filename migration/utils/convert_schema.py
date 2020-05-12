import json
import os
from typing import Dict

from migration.utils.collect_fields import list_path, typeof


def convert_schema(data: Dict[str, Dict]):
    """"""

    for k, v in data.items():
        """"""


def convert_all_schema(root_path):
    """"""

    def read(file):
        with open(file, 'r', encoding='utf-8') as reader:
            return json.loads(reader.read())

    paths = list(set([os.path.join('/', *i.split('/')[:-1]) for i in list_path(root_path)]))

    for path in paths:
        for i in os.listdir(path):
            if i == 'migrate_sorted.json':
                data = read(os.path.join(path, i))
                data = {k: v for k, v in sorted(data.items())}
                with open(f'{path}/aa.avsc', 'w', encoding='utf-8') as writer:
                    writer.write(json.dumps(data, indent=4, ensure_ascii=False))


class ConvertSchema(object):

    def __init__(self, path):
        self.path = path

    def read(self, file):
        with open(file, 'r', encoding='utf-8') as reader:
            return json.loads(reader.read())

    def write(self, path, data):
        with open(path, 'w', encoding='utf-8') as writer:
            writer.write(data)

    def typeof(self, variate, v):
        if variate == 'string':
            return 'string'
        elif variate == 'flog':
            return 'float'
        elif variate == 'int':
            return 'int'
        elif variate == 'list':
            items = list(set([typeof(i) for i in v]))

            return {
                'type': 'array',
                'items': items
            }

        elif variate == 'dict':
            """"""
            if len(v) == 1:
                if '$date' in v.keys():
                    return 'int'
                elif '$numberLong' in v.keys():
                    return 'float'
                elif '$oid' in v.keys():
                    return 'string'
                elif '$undefined' in v.keys():
                    if True in v.values():
                        return 'string'
                else:
                    raise Exception(f'Unknown infer type <{v}>')
            else:
                raise Exception(f'Unexcept len in <{v}>')

    def convert_fields(self, data: Dict[str, Dict]):
        fields = []
        for key, value in data.items():
            field = {'name': key}

            _type = []
            for k, v in value.items():
                """"""
                _type.append(self.typeof(k, v))
            if 'int' in _type and 'float' in _type:
                _type = ['float']

            if ('int' in _type and 'string' in _type) or ('float' in _type and 'string' in _type):
                raise Exception(f'Unknown infer type <{key}: {value}>')

            if key == 'date':
                field.update({"logicalType": "date"})
                field.update({'type': _type[0]})
            elif key == '_id':
                field.update({'type': _type[0]})
            else:
                _type.insert(0, 'null')
                field.update({'type': _type})
            fields.append(field)
        return fields

    def convert(self):
        paths = list(set([os.path.join('/', *i.split('/')[:-1]) for i in list_path(self.path)]))
        for path in paths:
            split_path = path.split('/')
            for i in os.listdir(path):
                if i == 'migrate_sorted.json':
                    print(f'Convert file {os.path.join(path, i)}')
                    print()
                    data = self.read(os.path.join(path, i))
                    fields = self.convert_fields(data)
                    data = {
                        'name': f'{split_path[-2]}',
                        'type': 'record',
                        'namespace': 'cn.tendata.customs.imports.dataset',
                        'fields': fields
                    }
                    data = json.dumps(data, indent=4, ensure_ascii=False)
                    self.write(os.path.join(path, f'{split_path[-2]}.avsc'), data)


if __name__ == '__main__':
    ConvertSchema('/data/customs/customs').convert()
