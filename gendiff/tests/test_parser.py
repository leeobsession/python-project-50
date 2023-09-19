from gendiff.parser import load_data
import pytest


FILES = [
    'gendiff/tests/fixtures/file1.json',
    'gendiff/tests/fixtures/file1.yml',
    'gendiff/tests/fixtures/file1.yaml'
]


@pytest.mark.parametrize('file', FILES)
def test_load_data(file):
    assert load_data(file) == {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False
    }
