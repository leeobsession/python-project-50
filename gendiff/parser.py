import yaml
import json
import os
import argparse


def load_data(path):
    _, ext = os.path.splitext(path)
    with open(path, 'r') as file:
        if ext == '.json':
            data = json.load(file)
        elif ext in ['.yml', '.yaml']:
            data = yaml.safe_load(file)
        else:
            raise ValueError(f'Unsupported file format: {ext}')
        return data


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument(
        '-f', '--format', metavar='FORMAT',
        help='set format of output', default='stylish')
    args = parser.parse_args()
    return args
