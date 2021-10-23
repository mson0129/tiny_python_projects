#!/usr/bin/env python3
"""
Author : michaelson <michaelson@localhost>
Date   : 2021-10-23
Purpose: Password maker
"""

import argparse
import random
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)',
                        type=argparse.FileType('rt'),
                        nargs='+')

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num_passwords',
                        type=int,
                        default=3)

    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words to use for password',
                        metavar='num_words',
                        type=int,
                        default=4)

    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum word length',
                        metavar='minimum',
                        type=int,
                        default=3)

    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maximum word length',
                        metavar='maximum',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate letters',
                        action='store_true',
                        default=False)

    args = parser.parse_args()

    if args.num < 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    if args.num_words < 0:
        parser.error(f'--num_words "{args.num_words}" must be greater than 0')

    if args.min_word_len < 0:
        parser.error(f'--min_word_len "{args.min_word_len}" must be greater than 0')
    
    if args.max_word_len < args.min_word_len:
        parser.error(f'--max_word_len "{args.max_word_len}" must be greater than {args.min_word_len}')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    random.seed(args.seed)
    words = set()

    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len

    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.lower().split())):
                words.add(word[0].upper() + word[1:])
    
    words = sorted(words)

    passwords: list = [''.join(random.sample(words, k=args.num_words)) for __ in range(0, args.num)]
    if args.l33t:
        passwords = [l33t(password) for password in passwords]
    print('\n'.join(passwords))

    # print('\n'.join([l33t(''.join(random.sample(words, k=args.num_words))) if args.l33t else ''.join(random.sample(words, k=args.num_words)) for __ in range(0, args.num)]))


# --------------------------------------------------
def clean(word):
    return re.sub(r'[^A-Za-z0-9]', '', word)


# --------------------------------------------------
def choose(char: str):
    return random.choice([char.lower(), char.upper()])


# --------------------------------------------------
def ransom(text: str):
    return ''.join([choose(char) for char in text])


# --------------------------------------------------
def l33t(text: str):
    replacer: dict = {
        'a': '@',
        'A': '4',
        'O': '0',
        't': '+',
        'E': '3',
        'I': '1',
        'S': '5'
    }
    return ''.join([replacer[char] if char in replacer else char for char in ransom(text)]) + random.choice(string.punctuation)


# --------------------------------------------------
if __name__ == '__main__':
    main()
