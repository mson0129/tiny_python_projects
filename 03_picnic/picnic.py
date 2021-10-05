#!/usr/bin/env python3
"""
Author : Michael Son <mson0129@gmail.com>
Date   : 2021-09-30
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    sorted = args.sorted

    if sorted:
        items.sort()

    if len(items) == 1:
        text = items[0]
    else:
        items[-1] = 'and ' + items[-1]
        text = ', '.join(items) if len(items) > 2 else ' '.join(items)
    
    print(f'You are bringing {text}.')

# --------------------------------------------------
if __name__ == '__main__':
    main()
