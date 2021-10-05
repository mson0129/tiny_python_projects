#!/usr/bin/env python3
"""
Author : Michael Son <mson0129@gmail.com>
Date   : 2021-10-02
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='file',
                        type=argparse.FileType('wt'),
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text_arg = args.text
    file_arg = args.outfile

    if os.path.isfile(text_arg):
        with open(text_arg, 'rt', encoding='UTF-8') as f:
            text_arg = f.read()
    text_arg = text_arg.upper()

    if file_arg:
        with open(file_arg.name, 'wt', encoding='UTF-8') as f:
            f.write(text_arg)
    else:
        print(text_arg)

# --------------------------------------------------
if __name__ == '__main__':
    main()
