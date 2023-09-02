import json


def make(val):
    result = json.dumps(val, sort_keys=True, indent=4)
    return result
