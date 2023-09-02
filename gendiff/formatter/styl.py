START_INDENT = 4
INDENT = ' '
MARKERS = {
    'added': '  + ',
    'removed': '  - ',
    'nothing': '    '
}


def stringify(value, depth=0):
    if isinstance(value, dict):
        result = ['{']
        for key, nest_value in value.items():
            if isinstance(nest_value, dict):
                new_value = stringify(nest_value, depth + START_INDENT)
                result.append(f'{INDENT * depth}    {key}: {new_value}')
            else:
                result.append(f'{INDENT * depth}    {key}: {nest_value}')
        result.append(f'{INDENT * depth}}}')
        return '\n'.join(result)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def build_string(depth, marker, key, value):
    return f'{INDENT * depth}{MARKERS[marker]}{key}: ' \
           f'{stringify(value, depth + START_INDENT)}'


def make_stylish(tree, depth=0): 
    result = ['{']
    for node in tree:
        if node['type'] == 'identical':
            result.append(build_string(
                depth, 'nothing', node['key'], node['value']
            ))

        elif node['type'] == 'added':
            result.append(build_string(
                depth, 'added', node['key'], node['value']
            ))

        elif node['type'] == 'removed':
            result.append(build_string(
                depth, 'removed', node['key'], node['value']
            ))

        elif node['type'] == 'changed':
            result.append(build_string(
                depth, 'removed', node['key'], node['old_value']
            ))
            result.append(build_string(
                depth, 'added', node['key'], node['new_value']
            ))

        elif node['type'] == 'nested':
            result.append(
                f"{INDENT * depth}    {node['key']}:"
                f" {format_to_stylish(node['children'], depth + START_INDENT)}")

    result.append(f'{INDENT * depth}}}')
    return '\n'.join(result)