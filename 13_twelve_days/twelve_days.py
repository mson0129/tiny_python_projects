#!/usr/bin/env python3
"""
Author : michaelson <michaelson@localhost>
Date   : 2021-10-14
Purpose: Rock the Casbah
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        default=sys.stdout)

    args = parser.parse_args()
    if args.num < 0 or args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    verses = []
    for day in range(1, args.num + 1):
        verses.append(verse(day))

    print('\n\n'.join(verses), file=args.outfile)


# --------------------------------------------------
def verse(day: int):
    """Create a verse"""
    ordinal = [
        'first',
        'second',
        'third',
        'fourth',
        'fifth',
        'sixth',
        'seventh',
        'eighth',
        'ninth',
        'tenth',
        'eleventh',
        'twelfth'
    ]
    verse: list = [
        f'On the {ordinal[day-1]} day of Christmas,',
        'My true love gave to me,'
    ]
    presents: list = [
        'A partridge in a pear tree',
        'Two turtle doves',
        'Three French hens',
        'Four calling birds',
        'Five gold rings',
        'Six geese a laying',
        'Seven swans a swimming',
        'Eight maids a milking',
        'Nine ladies dancing',
        'Ten lords a leaping',
        'Eleven pipers piping',
        'Twelve drummers drumming'
    ]
    for n in range(day-1, -1, -1):
        if day > 1 and n == 0:
            verse.append(f'And {presents[n].lower()}.')
        elif day == 1 and n == 0:
            verse.append(f'{presents[n]}.')
        else:
            verse.append(f'{presents[n]},')
    return '\n'.join(verse)


# --------------------------------------------------
def test_verse():
    """Test verse"""
    
    assert verse(1) == '\n'.join([
        'On the first day of Christmas,',
        'My true love gave to me,',
        'A partridge in a pear tree.'
    ])

    assert verse(2) == '\n'.join([
        'On the second day of Christmas,',
        'My true love gave to me,',
        'Two turtle doves,',
        'And a partridge in a pear tree.'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
