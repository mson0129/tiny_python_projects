#!/usr/bin/env python3
"""
Author : michaelson <michaelson@localhost>
Date   : 2021-10-23
Purpose: Create Workout Of (the) Day (WOD)
"""

import argparse
import csv
import random
import io
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Purpose: Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of excercise',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='excercises',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true',
                        default=False)

    args = parser.parse_args()

    if args.num < 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    
    exercises = read_csv(args.file)
    wod: list = []
    for exercise in random.sample(exercises, args.num):
        reps = random.randint(exercise[1], exercise[2])
        if args.easy:
            reps = int(reps/2)
        wod.append((exercise[0], reps))
    
    print(tabulate(wod, headers=('Exercise', 'Reps')))


# --------------------------------------------------
def read_csv(f):
    """Read the CSV Input"""
    reader = csv.DictReader(f, delimiter=',')
    exercises: list = []
    for record in reader:
        name, reps = record['exercise'], record['reps']
        low, high = reps.split('-')
        exercises.append((name, int(low), int(high)))
    return exercises


# --------------------------------------------------
def test_read_csv():
    """Test read_csv"""
    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
