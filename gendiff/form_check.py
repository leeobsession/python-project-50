from gendiff.formatter.styl import make_stylish
from gendiff.formatter.plain import make_plain
from gendiff.formatter.json import make_json


def format(tree, format_name):
    if format_name == 'stylish':
        return make_stylish(tree)
    elif format_name == 'plain':
        return make_plain(tree)
    elif format_name == 'json':
        return make_json(tree)
    else:
        raise ValueError('Unsupported format')
