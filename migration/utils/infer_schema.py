import json
import logging
from enum import Enum
from typing import List, Dict

# logging.getLogger(__name__)
from pymongo import MongoClient
from pymongo.database import Database, Collection


class InferSchema(object):

    def __init__(self, obj, name):
        self.obj = obj
        self.name = name
        self.namespace = 'com.infer'
        self.depth = 0

    def infer_schema(self, obj=None, name=None):
        self.depth += 1
        if self.depth == 1:
            name = self.name
            namespace = self.namespace
        else:
            namespace = ''

        if not obj and self.depth == 1:
            obj = self.obj

        if obj is None:
            inferred = 'null'
        elif isinstance(obj, bool):
            inferred = 'boolean'
        elif isinstance(obj, int):
            inferred = 'int'
        elif isinstance(obj, float):
            inferred = 'float'
        elif isinstance(obj, bytes):
            inferred = 'bytes'
        elif isinstance(obj, str):
            inferred = 'string'
        elif isinstance(obj, list):
            inferred = self._infer_array(obj, name)
        elif isinstance(obj, set):
            inferred = self._infer_array(obj, name)
        elif isinstance(obj, tuple):
            inferred = self._infer_array(obj, name)
        elif isinstance(obj, dict):
            """"""
            inferred = self._infer_record(obj, name, namespace)
        else:
            raise Exception(f'Infer Error . <{obj}> is Unknown type')
        return inferred

    def _infer_array(self, obj, name):

        items = []
        item_dict = []
        for i in obj:
            item = self.infer_schema(i)
            if isinstance(item, dict):
                item_dict.append(item)
            else:
                items.append(item)

        _items = list(set(items))
        _items.sort(key=items.index)
        if item_dict:
            _items.append(self.__merge_record(item_dict, name))

        return {
            'type': 'array',
            'items': _items
        }

    def __merge_record(self, records: List[Dict], name):
        """
        {
            "e": [{
                "xx": 0,
                "yy": 2
            }, {
                "ZZ": 1.10
            }]
        }



        {
            "name": "e",
            "type": {
                "type": "array",
                "items": {
                    "type": "record",
                    "name": "e",
                    "namespace": "",
                    "fields": [{
                        "name": "xx",
                        "type": ["null", "int"],
                        "doc": "Type inferred from '0'",
                        "default": null
                    }, {
                        "name": "yy",
                        "type": ["null", "int"],
                        "doc": "Type inferred from '2'",
                        "default": null
                    }, {
                        "name": "ZZ",
                        "type": ["null", "double", "boolean"],
                        "doc": "Type inferred from '1.1'",
                        "default": null
                    }]
                }
            },
            "doc": "Type inferred from '[{\"xx\":0,\"yy\":2},{\"ZZ\":1.1},{\"ZZ\":true}]'"
        }
        :param records:
        :return:
        """
        merged_name = name
        merged_fields = {}
        for record in records:
            for field in record.get('fields'):
                _name = field.get('name')
                _type = field.get('type')
                if _name in merged_fields.keys():
                    merged_field_type = merged_fields.get(_name)
                    if _type not in merged_field_type:
                        merged_field_type.append(_type)
                else:
                    merged_field_type = ['null', _type]
                merged_fields.update({_name: merged_field_type})
        return {
            'name': merged_name,
            'type': 'record',
            'namespace': '',
            'fields': [{'name': key, 'type': value, 'default': None} for key, value in sorted(merged_fields.items())]
        }

    def _infer_record(self, obj, name, namespace=''):
        return {
            'name': name,
            'type': 'record',
            'namespace': namespace,
            'fields': [
                {'name': k, 'type': self.infer_schema(v, k)}
                for k, v in sorted(obj.items())  # Sort fields by name.
            ]

        }


class MigrateSchema(object):
    """"""


if __name__ == '__main__':
    """"""
    data = {
        'a': [
            {'a1': 1},
            {'a2': 2},
            {'a1': 'a', 'a3': 2}
        ]
    }

    # res = InferSchema(data, 'test').infer_schema()
    # print(json.dumps(res, indent=4))

    # a = ['null', 'int', 'string', 'boolean', 'boolean', ]
    # a_ = list(set(a))
    # a_.sort(key=a.index)
    # print(a_)

    client = MongoClient('mongodb://192.168.2.223:27018')
    db = Database(client, 'bbb')
    col = Collection(db, 'business_company')
    res = col.find(limit=100)
    for i in res:
        i.pop('_id')
        schema = InferSchema(i, 'bbb').infer_schema()

        print(json.dumps(schema, indent=4, ensure_ascii=False))
        print()
