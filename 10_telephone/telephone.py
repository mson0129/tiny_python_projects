#!/usr/bin/env python3
"""
Author : Michael Son <mson0129@gmail.com>
Date   : 2021-10-09
Purpose: Rock the Casbah
"""

import argparse
import random
import os
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
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

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if args.mutations < 0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    if os.path.isfile(args.text):
        with open(args.text, "rt") as f:
            text = f.read()
    else:
        text = args.text
    text = text.strip()

    print(f'You said: "{text}"')

    # Mutations
    num_mutations = round(len(text) * args.mutations)

    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))

    indexes = random.sample(range(len(text)), num_mutations)

    for i in indexes:
        text = text[:i] + random.choice(alpha.replace(text[i], '')) + text[i+1:]

    print(f'I heard : "{text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
