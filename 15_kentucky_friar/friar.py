#!/usr/bin/env python3
"""
Author : michaelson <michaelson@localhost>
Date   : 2021-10-16
Purpose: Southern fry text
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text, 'rt', encoding='UTF-8') as f:
            args.text = f.read()
            args.text = args.text.strip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.text.splitlines():
        words = []
        for word in re.split(r'(\W+)', line):
            words.append(fry(word))
        print(''.join(words))


# --------------------------------------------------
def fry(word):
    if word.lower() == 'you':
        word = f'{word[:1]}\'all'
    elif any(c in 'aeiouy' for c in word.lower()[:-3]) and word[-3:] == 'ing':
        word = f'{word[:-1]}\''
    return word


# --------------------------------------------------
def test_fry():
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"



# --------------------------------------------------
if __name__ == '__main__':
    main()
