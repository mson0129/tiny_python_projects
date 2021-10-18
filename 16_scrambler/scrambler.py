#!/usr/bin/env python3
"""
Author : Michael Son <mson0129@gmail.com>
Date   : 2021-10-18
Purpose: Scramble the letters of words
"""

import argparse
import os
import re
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')
    
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()
    
    if os.path.isfile(args.text):
        with open(args.text, 'rt', encoding='UTF-8') as f:
            args.text = f.read().strip()
    
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    random.seed(args.seed)

    splitter = re.compile(r'''([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)''')
    for line in args.text.splitlines():
        print(''.join(map(scramble, splitter.split(line))))


# --------------------------------------------------
def scramble(word):
    """Scramble a word"""
    if len(word) > 3:
        middle: list = list(word[1:-1])
        random.shuffle(middle)
        word = word[0] + ''.join(middle) + word[-1]
    return word


# --------------------------------------------------
def test_scramble():
    """Test scramble"""
    state = random.getstate()
    random.seed(1)
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
