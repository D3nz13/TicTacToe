import numpy as np

PLAYER_ID = 1
BOT_ID = -1

class Board:
    def __init__(self, size=3):
        self.board = np.zeros((size, size))
        self.size = size
        self.game_over = False
    
    def get_valid_moves(self, state):
        """
        This method returns an array of all valid moves (a move is valid if the chosen place is empty)
        """
        return np.array(np.where(state == 0)).T
    
    def is_over(self, state):
        """
        This method checks if any of the players won by checking if any row/column/diagonal is filled with the same value and the value is not 0
        """
        transposed_board = state.T
        left_right_diag = state.diagonal()
        right_left_diag = np.flip(state, axis=0).diagonal()

        for row in state:  # checking by rows
            if np.all((row == row[0]) & (row[0] != 0)):
                return True
        for col in transposed_board:  # checking by columns
            if np.all((col == col[0]) & (col[0] != 0)):
                return True
        if np.all((left_right_diag == left_right_diag[0]) & (left_right_diag[0] != 0)):  # checking the diagonal coming from the left upper corner
            return True
        if np.all((right_left_diag == right_left_diag[0]) & (right_left_diag[0] != 0)):  # checking the diagonal coming from the right upper corner
            return True
        if len(self.get_valid_moves(state)) == 0:
            return True
        return False
    
    def valid_move(self, state, cords):
        """
        Checks if the move is valid
        """
        valid_moves = self.get_valid_moves(state)
        return any(np.array_equal(row, cords) for row in valid_moves)
    
    def make_move(self, cords, player):
        """
        Makes a move if valid
        """
        if self.valid_move(self.board, cords):
            self.board[cords[0]][cords[1]] = player
        else:
            raise Exception('Invalid move ! Try a new one')
    
    def does_win(self, state, player):
        """
        Checks if the player wins
        """
        transposed_board = state.T
        left_right_diag = state.diagonal()
        right_left_diag = np.flip(state, axis=0).diagonal()

        for row in state:  # checking by rows
            if np.all((row == row[0]) & (row[0] == player)):
                return True
        for col in transposed_board:  # checking by columns
            if np.all((col == col[0]) & (col[0] == player)):
                return True
        if np.all((left_right_diag == left_right_diag[0]) & (left_right_diag[0] == player)):  # checking the diagonal coming from the left upper corner
            return True
        if np.all((right_left_diag == right_left_diag[0]) & (right_left_diag[0] == player)):  # checking the diagonal coming from the right upper corner
            return True
        return False
    
    def evaluate(self, state):
        """
        Evaluates the score of the current board
        """
        if self.does_win(state, BOT_ID):
            return 1
        elif self.does_win(state, PLAYER_ID):
            return -1
        else:
            return 0
    
    def minimax(self, state, depth, player):
        """
        Finds the best move
        """
        all_moves = self.get_valid_moves(state)

        if player == BOT_ID:
            best = [-1, -1, -np.inf]
        else:
            best = [-1, -1, np.inf]
        
        if depth == 0 or self.is_over(state):
            return [-1, -1, self.evaluate(state)]
        
        for move in all_moves:
            x, y = move[0], move[1]
            state[x][y] = player
            score = self.minimax(state, depth-1, -player)
            state[x][y] = 0
            score[0], score[1] = x, y

            if player == BOT_ID:
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score
        
        return best
    
    def bot_turn(self):
        """
        Makes computer's turn
        """
        depth = len(self.get_valid_moves(self.board))
        if depth == 0 or self.is_over(self.board):
            return
        if depth == self.size**2:
            x = np.random.randint(0, self.size)
            y = np.random.randint(0, self.size)
        else:
            move = self.minimax(self.board, depth, BOT_ID)
            x, y = move[0], move[1]
        self.make_move([x, y], BOT_ID)
    
    def run(self):
        """
        Runs the game
        """
        while not(self.is_over(self.board)) and len(self.get_valid_moves(self.board) >= 1):
            self.bot_turn()
            print(self.board)
            while True:
                if self.is_over(self.board):
                    break
                x, y = list(map(int, input('What\'s your move?\n').split()))
                try:
                    self.make_move([x, y], PLAYER_ID)
                except Exception as e:
                    print(e)
                else:
                    break
        print(self.board)


if __name__ == '__main__':
    board = Board()
    board.run()