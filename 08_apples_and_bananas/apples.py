#!/usr/bin/env python3
"""
Author : Michael Son <mson0129@gmail.com>
Date   : 2021-10-06
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        choices=['a', 'e', 'i', 'o', 'u'],
                        default='a')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_capital = ['A', 'E', 'I', 'O', 'U']

    text: str = ''
    if os.path.isfile(args.text):
        with open(args.text, "rt", encoding="UTF-8") as f:
            text = f.read()
    else:
        text = args.text

    new: str = ''
    for char in text:
        if char in vowels:
            new += args.vowel.lower()
        elif char in vowels_capital:
            new += args.vowel.upper()
        else:
            new += char

    print(new)


# --------------------------------------------------
if __name__ == '__main__':
    main()
