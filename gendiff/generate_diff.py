from gendiff.parser import load_data
from gendiff.get import create_diff
from gendiff.form_check import format


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)
    formatted_data = create_diff(data1, data2)
    return format(formatted_data, format_name)
