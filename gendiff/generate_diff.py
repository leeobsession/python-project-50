from gendiff.parser import parser
from gendiff.get import create_diff
from gendiff.form_check import format


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parser(file_path1)
    data2 = parser(file_path2)
    formatted_data = create_diff(data1, data2)
    return format(format_name, formatted_data)