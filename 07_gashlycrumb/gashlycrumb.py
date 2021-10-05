#!/usr/bin/env python3
"""
Author : Michael Son <mson0129@gmail.com>
Date   : 2021-10-06
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    article: dict = {}
    for line in args.file:
        article[line[:1].lower()] = line

    for letter in args.letter:
        if letter.lower() in article:
            print(article[letter.lower()], end='')
        else:
            print(f'I do not know "{letter}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
