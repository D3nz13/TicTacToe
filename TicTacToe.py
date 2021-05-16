import numpy as np

class Board:
    def __init__(self, size=3):
        self.board = np.zeros((size, size))
        self.winner = None
    
    def get_valid_moves(self):
        """
        This method returns an array of all valid moves (a move is valid if the chosen place is empty)
        """
        return np.array(np.where(self.board == 0)).T
    
    def is_over(self):
        """
        This method checks if any of the players won by checking if any row/column/diagonal is filled with the same value and the value is not 0
        """
        transposed_board = self.board.T
        left_right_diag = self.board.diagonal()
        right_left_diag = np.flip(self.board, axis=0).diagonal()

        for row in self.board:  # checking by rows
            if np.all((row == row[0]) & (row[0] != 0)):
                self.winner = int(row[0])
                return True
        for col in transposed_board:  # checking by columns
            if np.all((col == col[0]) & (col[0] != 0)):
                self.winner = int(col[0])
                return True
        if np.all((left_right_diag == left_right_diag[0]) & (left_right_diag[0] != 0)):  # checking the diagonal coming from the left upper corner
            self.winner = int(left_right_diag[0])
            return True
        if np.all((right_left_diag == right_left_diag[0]) & (right_left_diag[0] != 0)):  # checking the diagonal coming from the right upper corner
            self.winner = int(right_left_diag[0])
            return True
        return False
    
    def valid_move(self, cords):
        """
        Checks if the move is valid
        """
        valid_moves = self.get_valid_moves()
        return any(np.array_equal(row, cords) for row in valid_moves)
    
    def make_move(self, cords, player):
        """
        Makes a move if valid
        """
        if self.valid_move(cords):
            self.board[cords[0], cords[1]] = player
        else:
            raise Exception('Invalid move ! Try a new one')


if __name__ == '__main__':
    board = Board()
    board.board[0, 0] = 1
    board.board[1, 0] = 1
    board.board[2, 0] = 1
    board.board[1, 2] = 2
    board.board[2, 0] = 1
    print(board.board)
    board.make_move([0, 1], 1)
    print(board.board)