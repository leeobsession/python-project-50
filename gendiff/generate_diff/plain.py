def get_val(val):
    if isinstance(val, dict):
        return '[complex value]'

    elif val is None:
        return 'null'

    elif isinstance(val, bool):
        return 'true' if val else 'false'

    elif isinstance(val, str):
        return f"'{val}'"

    else:
        return val


def make_plain(data, path=[]):
    output = ''

    for key, val in data.items():
        types = val.get('type')
        values = val.get('value')
        children = val.get('children')
        path_copy = path.copy()
        path_copy.append(key)

        if types == 'added':
            output += f"Property '{'.'.join(path_copy)}'" \
                      f" was added with value: {get_val(values)}\n"

        elif types == 'removed':
            output += f"Property '{'.'.join(path_copy)}' was removed\n"

        elif types == 'changed':
            old = get_val(values.get('old_value'))
            new = get_val(values.get('new_value'))
            output += f"Property '{'.'.join(path_copy)}' was updated." \
                      f" From {old} to {new}\n"

        elif types == 'dictionary':
            output += f"{make_plain(children, path_copy)}\n"

    return output.strip()
