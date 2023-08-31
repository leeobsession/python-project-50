from gendiff.gendiff import generate_diff


def test_generate_diff():

    data1 = 'gendiff/tests/fixtures/file_json1.json'
    data2 = 'gendiff/tests/fixtures/file_json2.json'

    result_json = \
        open('gendiff/tests/fixtures/result_json.txt').read()
    result_stylish = \
        open('gendiff/tests/fixtures/result_stylish.txt').read()
    result_plain = \
        open('gendiff/tests/fixtures/result_plain.txt').read()

    diff_json1 = generate_diff(data1, data2)
    diff_json2 = generate_diff(data1, data1)
    diff_plain = generate_diff(data1, data2, 'plain')

    assert generate_diff(data1, data2, 'stylish') == result_stylish
    assert generate_diff(data1, data2) == result_stylish
    assert generate_diff(data1, data2, 'plain') == result_plain
    assert generate_diff(data1, data2, 'json') == result_json
