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


FILES_PARSER = [
    'tests/fixtures/file1.json',
    'tests/fixtures/file1.yml',
    'tests/fixtures/file1.yaml'
]
