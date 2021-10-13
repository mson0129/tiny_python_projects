#!/usr/bin/env python3
"""
Author : Michael Son <mson0129@gmail.com>
Date   : 2021-10-13
Purpose: Rock the Casbah
"""

import argparse
import random
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    if os.path.isfile(args.text):
        with open(args.text, "rt", encoding='UTF-8') as f:
            text = f.read()
    else:
        text = args.text
    text = text.strip()

    # Version "For"
    # new_text: str = ''
    # for char in text:
    #     print(choose(char), end='')

    # Version "list"
    # print(''.join([choose(char) for char in text]))

    # Version "map"
    print(''.join(map(choose, text)))


# --------------------------------------------------
def choose(char: str):
    return random.choice([char.lower(), char.upper()])


# --------------------------------------------------
def test_choose():
    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'c'
    assert choose('d') == 'd'
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
