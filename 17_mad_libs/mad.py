#!/usr/bin/env python3
"""
Author : Michael Son <mson0129@gmail.com>
Date   : 2021-10-20
Purpose: Mad Libs
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='file',
                        help='Input file',
                        type=argparse.FileType('rt'))

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        nargs='*',
                        metavar='input',
                        type=str,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.file.read().rstrip()
    args.file.close()
    matches = re.findall(r'(<([^<>]+)>)', text)

    if len(matches) == 0:
        sys.exit(f'"{args.file.name}" has no placeholders.')

    if args.inputs:
        inputs = args.inputs
    else:
        inputs = []

    if len(inputs) < len(matches):
        for i in range(len(inputs), len(matches)):
            article = 'an' if matches[i][1][:1] in 'aeiou' else 'a'
            value = input(f'Give me {article} {matches[i][1]}: ')
            inputs.append(value)
    
    for value in inputs:
        text = re.sub(r'(<([^<>]+)>)', repl=value, string=text, count=1)
    
    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
