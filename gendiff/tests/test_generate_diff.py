from gendiff.gendiff import gener_diff


def test_gener_diff():

    data1 = 'gendiff/tests/fixtures/file1.json'
    data2 = 'gendiff/tests/fixtures/file2.json'
    data3 = 'gendiff/tests/fixtures/file_json1.json'
    data4 = 'gendiff/tests/fixtures/file_json2.json'

    result_json1 = \
        open('gendiff/tests/fixtures/result_json.txt').read()
    result_json2 = \
        open('gendiff/tests/fixtures/result_json1.txt').read()
    result_plain = \
        open('gendiff/tests/fixtures/result_plain.txt').read()

    diff_json1 = gener_diff(data1, data2)
    diff_json2 = gener_diff(data3, data4)
    diff_plain = gener_diff(data1, data2, 'plain')

    assert diff_json1 == result_json1
    assert diff_json2 == result_json2
    assert result_plain == diff_plain
