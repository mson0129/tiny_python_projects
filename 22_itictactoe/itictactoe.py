#!/usr/bin/env python3
"""
Author : michaelson <michaelson@localhost>
Date   : 2021-10-26
Purpose: Rock the Casbah
"""

# --------------------------------------------------
class TicTacToe:
    debug: bool = False
    board: list = list('.' * 9)
    activePlayer: str = 'X'
    quit: bool = False
    error: bool = False
    winning: list = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]


    def print_board(self) -> None:
        horizontal_border: str = '-------------'
        vertical_border: str = ' | '
        print(horizontal_border)
        for i in range(0, 3):
            print((
                vertical_border
                + vertical_border.join([self.board[cell] if self.board[cell] != '.' else str(cell+1) for cell in range(i*3, (i+1)*3)])
                + vertical_border
            ).strip())
            print(horizontal_border)
    

    def response(self, user_input = None) -> None:
        if user_input.lower() == 'q':
            self.quit = True
        elif user_input not in [str(i) for i in range(1, 10)]:
            self.print_board()
            print(f'Invalid cell {user_input}, please use 1-9.')
        elif self.board[int(user_input)-1] != '.':
            self.print_board()
            print(f'Cell "{user_input}" already taken.')
        else:
            self.board[int(user_input)-1] = self.activePlayer
            self.print_board()
            self.activePlayer = 'X' if self.activePlayer == 'O' else 'O'


    def check_draw(self) -> bool:
        isDraw: bool = False
        if '.' not in self.board:
            isDraw = True
        else:
            winning = list(self.winning)
            for cell in [k for k, v in enumerate(self.board) if v not in ['.', self.activePlayer]]:
                if self.debug:
                    print(f'cell: {cell}')
                winning = [win for win in winning if cell not in win]
            if self.debug:
                print(f'winning len: {len(winning)}')
            if len(winning) == 0:
                isDraw = True
        return isDraw
    

    def check_winner(self):
        winner = None
        for player in ['X', 'O']:
            for i, j, k in self.winning:
                if [self.board[i], self.board[j], self.board[k]] == list(player * 3):
                    winner = player
                    break
            if winner is not None:
                break
        return winner


    def loop(self) -> None:
        self.print_board()
        while(True):
            user_input: str = input(f'Player {self.activePlayer}, what is your move? [q to quit]:')
            self.response(user_input)
            
            winner = self.check_winner()
            if winner is not None:
                print(f'{winner} has won!')
                self.quit = True
            elif self.check_draw():
                print(f'Draw')
                self.quit = True
            
            if self.quit:
                break


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    c = TicTacToe()
    c.loop()


# --------------------------------------------------
if __name__ == '__main__':
    main()
