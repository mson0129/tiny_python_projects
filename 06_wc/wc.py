#!/usr/bin/env python3
"""
Author : Michael Son <mson0129@gmail.com>
Date   : 2021-10-04
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word cound)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total_num_lines: int = 0
    total_num_words: int = 0
    total_num_bytes: int = 0

    for fh in args.file:
        num_lines: int = 0
        num_words: int = 0
        num_bytes: int = 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)
        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}')
        total_num_lines += num_lines
        total_num_words += num_words
        total_num_bytes += num_bytes
    
    if len(args.file) > 1:
        print(f'{total_num_lines:8}{total_num_words:8}{total_num_bytes:8} total')

# --------------------------------------------------
if __name__ == '__main__':
    main()
