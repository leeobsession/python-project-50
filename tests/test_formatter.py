from gendiff.formatter.styl import stringify
from gendiff.formatter.plain import stringify

def test_formatter():
    assert stringify(True) == 'true'
    assert stringify(False) == 'false'
    assert stringify(20) == '20'
