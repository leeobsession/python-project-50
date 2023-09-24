from gendiff.parser import load_data
from tests.fixtures import testing_constants
import pytest


@pytest.mark.parametrize('file', testing_constants.FILES_PARSER)
def test_load_data(file):
    assert load_data(file) == {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False
    }
