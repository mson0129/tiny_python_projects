#! /usr/bin/env python3
"""
Author: Michael Son(mson0129@gmail.com)
Purpose: Say hello
"""

import argparse


def get_args():
    """doc"""
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """doc"""
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
