from gendiff.generate_diff import generate_diff
import pytest
import os


FILES = [
    ('file1.json', 'file2.json', 'result_stylish.txt', 'stylish'),
    ('file1.json', 'file2.json', 'result_plain.txt', 'plain'),
    ('file1.json', 'file2.json', 'result_json.txt', 'json'),
    ('file1.yml', 'file2.yml', 'result_stylish.txt', 'stylish'),
    ('file1.yml', 'file2.yml', 'result_plain.txt', 'plain'),
    ('file1.yml', 'file2.yml', 'result_json.txt', 'json'),
    ('file1.yaml', 'file2.yaml', 'result_stylish.txt', 'stylish'),
    ('file1.yaml', 'file2.yaml', 'result_plain.txt', 'plain'),
    ('file1.yaml', 'file2.yaml', 'result_json.txt', 'json'),
    ('file3.json', 'file4.json', 'result_stylish2.txt', 'stylish'),
    ('file3.json', 'file4.json', 'result_plain2.txt', 'plain'),
    ('file3.json', 'file4.json', 'result_json2.txt', 'json'),
    ('file3.yml', 'file4.yml', 'result_stylish2.txt', 'stylish'),
    ('file3.yml', 'file4.yml', 'result_plain2.txt', 'plain'),
    ('file3.yml', 'file4.yml', 'result_json2.txt', 'json'),
    ('file3.yaml', 'file4.yaml', 'result_stylish2.txt', 'stylish'),
    ('file3.yaml', 'file4.yaml', 'result_plain2.txt', 'plain'),
    ('file3.yaml', 'file4.yaml', 'result_json2.txt', 'json')
]

FILES_EXCEPTION = [
    ('file1.json', 'file2.json', 'txt'),
    ('file3.yml', 'file4.yml', 'doc')
]

FILES_EXCEPTION2 = [
    ('file1.txt', 'file2.json')
]


def get_path(filename):
    return os.path.join('tests/fixtures', filename)


@pytest.mark.parametrize('file1, file2, result, formatter', FILES)
def test_generate_diff(file1, file2, result, formatter):
    with open(get_path(result), 'r') as res:
        result_string = '\n'.join(res.read().splitlines())
    diff = generate_diff(get_path(file1), get_path(file2), formatter)
    assert diff == result_string


@pytest.mark.parametrize('file1, file2, formatter', FILES_EXCEPTION)
def test_exception(file1, file2, formatter):
    with pytest.raises(ValueError) as e:
        generate_diff(
            get_path(file1),
            get_path(file2),
            formatter)
        assert str(e.value) == 'Unsupported format'


@pytest.mark.parametrize('file1, file2', FILES_EXCEPTION2)
def test_exception2(file1, file2):
    with pytest.raises(ValueError) as e:
        generate_diff(
            get_path(file1),
            get_path(file2))
        assert str(e.value) == 'Unsupported file format: txt'
