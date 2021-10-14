#! /usr/bin/env python3
"""
Author : Michael Son <mson0129@gmail.com>
Date   : 2021-09-28
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    word = args.word
    char = word[0].lower()
    article = 'an' if char in 'aeiou' else 'a'
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')

# --------------------------------------------------
if __name__ == '__main__':
    main()
