#!/usr/bin/env python3
"""
Author : michaelson <michaelson@localhost>
Date   : 2021-10-25
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--board',
                        help='Board Status',
                        metavar='board',
                        type=str,
                        default='.' * 9)

    parser.add_argument('-p',
                        '--player',
                        help='Player',
                        metavar='player',
                        type=str,
                        choices=['X', 'O'])

    parser.add_argument('-c',
                        '--cell',
                        help='Cell',
                        metavar='cell',
                        type=int,
                        choices=range(1, 10))

    args = parser.parse_args()

    if len(args.board) != 9:
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')

    if (args.player is None) != (args.cell is None):
        parser.error(f'Must provide both --player and --cell')

    if (args.cell is not None) and (args.board[args.cell - 1] != '.'):
        parser.error(f'--cell "{args.cell}" already taken')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if args.player is not None:
        board = ''.join([args.board[i] if args.cell != i + 1 else args.player for i in range(0, 9)])
    else:
        board = args.board
    print(format_board(board))
    winner = find_winner(board)
    if winner is None:
        print(f'No winner.')
    else:
        print(f'{winner} has won!')


# --------------------------------------------------
def format_board(board: str):
    horizontal_border = '-' * 13
    vertical_border = ' | '
    
    rows: list = []
    rows.append(horizontal_border)
    for row_index in range(0, 3):
        row = (vertical_border + vertical_border.join([board[cell] if board[cell] != '.' else str(cell + 1) for cell in range(row_index * 3, (row_index + 1) * 3)]) + vertical_border).strip()
        rows.append(row)
        rows.append(horizontal_border)
    
    return '\n'.join(rows)


# --------------------------------------------------
def find_winner(board):
    # to rewrite code using method of elimination

    winner: str = None
    
    for i in range(0, 3):
        # horizontal
        if (board[i*3] == board [i*3+1]) and (board[i*3] == board [i*3+2]) and (board[i*3] != '.'):
            winner = board[i*3]
            break
        # vertical
        if (board[0*3+i] == board [1*3+i]) and (board[0*3+i] == board [2*3+i]) and (board[0*3+i] != '.'):
            winner = board[0*3 + i]
            break
        # diagonal
        if i != 1:
            if (board[0*(4-i)+i] == board[1*(4-i)+i]) and (board[0*(4-i)+i] == board[2*(4-i)+i]) and (board[0*(4-i)+i] != '.'):
                winner = board[0*(4-i)+i]
                break
    return winner


# --------------------------------------------------
if __name__ == '__main__':
    main()
