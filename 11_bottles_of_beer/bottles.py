#!/usr/bin/env python3
"""
Author : Michael Son <mson0129@gmail.com>
Date   : 2021-10-11
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)
    
    args = parser.parse_args()

    if args.number < 1:
        parser.error(f'--num "{args.number}" must be greater than 0')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for i in range(args.number, 0, -1):
        print(verse(i))
        if i > 1:
            print('')


# --------------------------------------------------
def verse(bottle: int):
    """Sing a verse"""

    if bottle > 2:
        verse = '\n'.join([
            f'{bottle} bottles of beer on the wall,',
            f'{bottle} bottles of beer,',
            'Take one down, pass it around,',
            f'{bottle-1} bottles of beer on the wall!',
        ])
    elif bottle == 2:
        verse = '\n'.join([
            f'{bottle} bottles of beer on the wall,',
            f'{bottle} bottles of beer,',
            'Take one down, pass it around,',
            f'{bottle-1} bottle of beer on the wall!',
        ])
    else: # bottle
        verse = '\n'.join([
            f'{bottle} bottle of beer on the wall,',
            f'{bottle} bottle of beer,',
            'Take one down, pass it around,',
            f'No more bottles of beer on the wall!'
        ])

    return verse


# --------------------------------------------------
def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,',
        '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,',
        '2 bottles of beer,',
        'Take one down, pass it around,',
        '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
