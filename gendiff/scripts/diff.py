#!/usr/bin/env python3
from gendiff.gendiff import gener_diff
from gendiff.parser import parse_args


def main():
    args = parse_args()
    print(gener_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()


# END
