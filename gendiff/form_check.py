from gendiff.generate_diff.styl import make_stylish
from gendiff.generate_diff.plain import make_plain
from gendiff.generate_diff.json import make


def format(form_name, form_data):
    if form_name == 'plain':
        return make_plain(form_data)
    elif form_name == 'json':
        return make(form_data)
    else:
        return make_stylish(form_data)
