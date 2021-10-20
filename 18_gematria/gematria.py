#!/usr/bin/env python3
"""
Author : michaelson <michaelson@localhost>
Date   : 2021-10-21
Purpose: Gematria
"""

import argparse
import os
import re
from functools import reduce


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text, 'rt', encoding='UTF-8') as f:
            args.text = f.read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.text.splitlines():
        print(' '.join(map(word2num, line.split())))


# --------------------------------------------------
def product(vals):
    return reduce(lambda x, y: x * y, vals)


# --------------------------------------------------
def join(separator: str, vals: list):
    return reduce(lambda x, y: x + separator + y, vals)


# --------------------------------------------------
def word2num(word):
    word = re.sub(r'[^A-Za-z0-9]', '', word)
    return str(sum(map(ord, word)))


# --------------------------------------------------
def test_word2num():
    """Test word2num"""
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"

# --------------------------------------------------
if __name__ == '__main__':
    main()
