from migration.utils.infer_schema import InferSchema

namespace = 'com.infer'


def test_infer1():
    data = {
        'a': None,
        'b': True,
        'c': 10,
        'd': 0.1,
        'e': b'e',
        'f': 'xxx',
    }
    schema = {
        'type': 'record',
        'name': 'test',
        'namespace': namespace,
        'fields': [
            {'name': 'a', 'type': 'null'},
            {'name': 'b', 'type': 'boolean'},
            {'name': 'c', 'type': 'int'},
            {'name': 'd', 'type': 'float'},
            {'name': 'e', 'type': 'bytes'},
            {'name': 'f', 'type': 'string'},
        ]
    }

    assert InferSchema(data, 'test').infer_schema() == schema


def test_infer_array():
    data = {
        'a': None,
        'b': True,
        'c': 10,
        'd': 0.1,
        'e': b'e',
        'f': 'xxx',
        'g': [1, '2', True]
    }
    schema = {
        'type': 'record',
        'name': 'test',
        'namespace': namespace,
        'fields': [
            {'name': 'a', 'type': 'null'},
            {'name': 'b', 'type': 'boolean'},
            {'name': 'c', 'type': 'int'},
            {'name': 'd', 'type': 'float'},
            {'name': 'e', 'type': 'bytes'},
            {'name': 'f', 'type': 'string'},
            {
                'name': 'g',
                'type': {
                    'type': 'array',
                    'items': ['int', 'string', 'boolean']
                }
            }
        ]
    }

    assert InferSchema(data, 'test').infer_schema() == schema


def test_infer_dict():
    data = {
        'a': None,
        'b': True,
        'c': 10,
        'd': 0.1,
        'e': b'e',
        'f': 'xxx',
        'g': {
            'g1': 1
        }
    }
    schema = {
        'type': 'record',
        'name': 'test',
        'namespace': namespace,
        'fields': [
            {'name': 'a', 'type': 'null'},
            {'name': 'b', 'type': 'boolean'},
            {'name': 'c', 'type': 'int'},
            {'name': 'd', 'type': 'float'},
            {'name': 'e', 'type': 'bytes'},
            {'name': 'f', 'type': 'string'},
            {
                'name': 'g',
                'type': {
                    'type': 'record',
                    'name': 'g',
                    'namespace': '',
                    'fields': [
                        {'name': 'g1', 'type': 'int'}
                    ]
                }
            }
        ]
    }
    assert InferSchema(data, 'test').infer_schema() == schema


def test_infer_list_dict():
    data = {
        'a': [
            {'a1': 1},
            {'a2': 2},
            {'a1': 'a1', 'a3': 'a3'}
        ]
    }

    schema = {
        'name': 'test',
        'type': 'record',
        'namespace': 'com.infer',
        'fields': [
            {
                'name': 'a',
                'type': {
                    'type': 'array',
                    'items': [
                        {
                            'name': 'a',
                            'type': 'record',
                            'namespace': '',
                            'fields': [
                                {'name': 'a1', 'type': ['null', 'int', 'string'], 'default': None},
                                {'name': 'a2', 'type': ['null', 'int'], 'default': None},
                                {'name': 'a3', 'type': ['null', 'string'], 'default': None},
                            ]
                        }
                    ]
                }
            }
        ]
    }

    assert InferSchema(data, 'test').infer_schema() == schema


def test_infer_set():
    data = {
        'a': None,
        'b': True,
        'c': 10,
        'd': 0.1,
        'e': b'e',
        'f': 'xxx',
        'g': {1, "a"}
    }
    schema = {
        'type': 'record',
        'name': 'test',
        'namespace': namespace,
        'fields': [
            {'name': 'a', 'type': 'null'},
            {'name': 'b', 'type': 'boolean'},
            {'name': 'c', 'type': 'int'},
            {'name': 'd', 'type': 'float'},
            {'name': 'e', 'type': 'bytes'},
            {'name': 'f', 'type': 'string'},
            {
                'name': 'g',
                'type': {
                    'type': 'array',
                    'items': ['int', 'string']
                }
            }
        ]
    }
    assert InferSchema(data, 'test').infer_schema() == schema


def test_infer_tuple():
    data = {
        'a': None,
        'b': True,
        'c': 10,
        'd': 0.1,
        'e': b'e',
        'f': 'xxx',
        'g': (1, 'a')
    }
    schema = {
        'type': 'record',
        'name': 'test',
        'namespace': namespace,
        'fields': [
            {'name': 'a', 'type': 'null'},
            {'name': 'b', 'type': 'boolean'},
            {'name': 'c', 'type': 'int'},
            {'name': 'd', 'type': 'float'},
            {'name': 'e', 'type': 'bytes'},
            {'name': 'f', 'type': 'string'},
            {
                'name': 'g',
                'type': {
                    'type': 'array',
                    'items': ['int', 'string']
                }
            }
        ]
    }
    assert InferSchema(data, 'test').infer_schema() == schema


def test_infer_hybrid():
    data = {
        'a': None,
        'b': True,
        'c': 10,
        'd': 0.1,
        'e': b'e',
        'f': 'xxx',
        'g': ['string', 1],
        'h': {
            'h1': 1,
            'h2': 'h2',
            'h3': [1, 2, 3],
            'h4': {
                'h4_1': '1'
            }
        },
        'i': [
            'a',
            {'i1': 1, 'i2': 2},
            {'i1': 'i1', 'i3': 'i3'}
        ]
    }
    schema = {
        'type': 'record',
        'name': 'test',
        'namespace': namespace,
        'fields': [
            {'name': 'a', 'type': 'null'},
            {'name': 'b', 'type': 'boolean'},
            {'name': 'c', 'type': 'int'},
            {'name': 'd', 'type': 'float'},
            {'name': 'e', 'type': 'bytes'},
            {'name': 'f', 'type': 'string'},
            {
                'name': 'g',
                'type': {
                    'type': 'array',
                    'items': ['string', 'int']
                }
            },
            {
                'name': 'h',
                'type': {
                    'name': 'h',
                    'type': 'record',
                    'namespace': '',
                    'fields': [
                        {'name': 'h1', 'type': 'int'},
                        {'name': 'h2', 'type': 'string'},
                        {
                            'name': 'h3',
                            'type': {
                                'type': 'array',
                                'items': ['int']
                            }
                        },
                        {
                            'name': 'h4',
                            'type': {
                                'name': 'h4',
                                'type': 'record',
                                'namespace': '',
                                'fields': [
                                    {'name': 'h4_1', 'type': 'string'}
                                ]
                            }
                        }
                    ]
                }
            },
            {
                'name': 'i',
                'type': {
                    'type': 'array',
                    'items': [
                        'string',
                        {
                            'name': 'i',
                            'type': 'record',
                            'namespace': '',
                            'fields': [
                                {'name': 'i1', 'type': ['null', 'int', 'string'], 'default': None},
                                {'name': 'i2', 'type': ['null', 'int'], 'default': None},
                                {'name': 'i3', 'type': ['null', 'string'], 'default': None},

                            ]
                        }
                    ]
                }
            }
        ]
    }
    assert InferSchema(data, 'test').infer_schema() == schema
