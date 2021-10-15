#!/usr/bin/env python3
"""
Author : michaelson <michaelson@localhost>
Date   : 2021-10-15
Purpose: Rock the Casbah
"""

import argparse
import string
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    separated_word: tuple = stemmer(args.word)

    if type(separated_word[1]) == None or separated_word[1] == '':
        print(f'Cannot rhyme "{args.word}"')
    else:
        consonants: list = [c for c in string.ascii_lowercase if c not in 'aeiou']
        consonants.extend('''bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st sw th tr tw thw wh wr sch scr shr sph spl spr squ str thr'''.split())
        consonants.sort()
        for c in consonants:
            if c != separated_word[0]:
                print(f'{c}{separated_word[1]}')


# --------------------------------------------------
def stemmer(word):
    """Return leading consonants (if any), and 'stem' of word"""
    return re.match(r'([^aeiou]*)(.*)', word.lower()).groups()


# --------------------------------------------------
def test_stemmer():
    """test the stemmer"""

    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')


# --------------------------------------------------
if __name__ == '__main__':
    main()
