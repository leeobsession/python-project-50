from gendiff.generate_diff import generate_diff
from tests.fixtures import testing_constants
import pytest
import os


def get_path(filename):
    return os.path.join('tests/fixtures', filename)


@pytest.mark.parametrize('file1, file2, result, formatter', testing_constants.FILES)
def test_generate_diff(file1, file2, result, formatter):
    with open(get_path(result), 'r') as res:
        result_string = '\n'.join(res.read().splitlines())
    diff = generate_diff(get_path(file1), get_path(file2), formatter)
    assert diff == result_string


@pytest.mark.parametrize('file1, file2, formatter', testing_constants.FILES_EXCEPTION)
def test_exception(file1, file2, formatter):
    with pytest.raises(ValueError) as e:
        generate_diff(
            get_path(file1),
            get_path(file2),
            formatter)
        assert str(e.value) == 'Unsupported format'


@pytest.mark.parametrize('file1, file2', testing_constants.FILES_EXCEPTION2)
def test_exception2(file1, file2):
    with pytest.raises(ValueError) as e:
        generate_diff(
            get_path(file1),
            get_path(file2))
        assert str(e.value) == 'Unsupported file format: txt'
