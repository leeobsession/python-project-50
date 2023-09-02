from gendiff.formatter.styl import make_stylish
from gendiff.formatter.plain import make_plain
from gendiff.formatter.json import make


def format(form_name, form_data):
    if form_name == 'plain':
        return make_plain(form_data)
    elif form_name == 'json':
        return make(form_data)
    elif form_name == 'stylish':
        return make_stylish(form_data)
    else:
        raise ValueError('Unsupported format')
