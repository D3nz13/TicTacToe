import numpy as np

class Board:
    def __init__(self, size=3):
        self.board = np.zeros((size, size))
    
    def get_valid_moves(self):  # returns all places that are occupied by neither of the players
        return np.array(np.where(self.board == 0)).T
    
    def is_over(self):
        transposed_board = self.board.T
        left_right_diag = self.board.diagonal()
        right_left_diag = np.flip(self.board, axis=0).diagonal()
        if np.any(np.all((self.board == self.board[0, :]) & (self.board[0, :] != 0), axis=0)):  # checking by cols
            return True
        elif np.any(np.all((transposed_board == transposed_board[0, :]) & (transposed_board[0, :] != 0), axis=0)):  # checking by rows
            return True
        elif np.all((left_right_diag == left_right_diag[0]) & (left_right_diag[0] != 0)):  # checking the diagonal coming from the left upper corner
            return True
        elif np.all((right_left_diag == right_left_diag[0]) & (right_left_diag[0] != 0)):  # checking the diagonal coming from the right upper corner
            return True
        return False


if __name__ == '__main__':
    board = Board()
    board.board[0, 2] = 2
    board.board[1, 1] = 2
    board.board[2, 0] = 2
    print(board.board)
    print(board.is_over())