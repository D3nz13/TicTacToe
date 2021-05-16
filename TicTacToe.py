import numpy as np

PLAYER_ID = 1
BOT_ID = 2

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
        This method checks if any of the players won by checking if any row/column/diagonal is filled with the same value and the value is not 0, also returns the winner
        """
        transposed_board = state.T
        left_right_diag = state.diagonal()
        right_left_diag = np.flip(state, axis=0).diagonal()

        for row in state:  # checking by rows
            if np.all((row == row[0]) & (row[0] != 0)):
                return (True, int(row[0]))
        for col in transposed_board:  # checking by columns
            if np.all((col == col[0]) & (col[0] != 0)):
                return (True, int(col[0]))
        if np.all((left_right_diag == left_right_diag[0]) & (left_right_diag[0] != 0)):  # checking the diagonal coming from the left upper corner
            return (True, int(left_right_diag[0]))
        if np.all((right_left_diag == right_left_diag[0]) & (right_left_diag[0] != 0)):  # checking the diagonal coming from the right upper corner
            return (True, int(right_left_diag[0]))
        return (False, None)
    
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
            self.board[cords[0], cords[1]] = player
        else:
            raise Exception('Invalid move ! Try a new one')
    
    def evaluate_score(self, state, player):
        """
        Evaluates the score of the current 
        """
        is_over, winner = self.is_over(state)
        if is_over and winner == player:
            return 1
        elif is_over:
            return -1
        else:
            return 0
    
    def minimax(self, state, depth, player):
        """
        Finds the best move
        """
        if depth == 0 or self.game_over:
            return (self.evaluate_score(state, player), None)
        
        all_moves = self.get_valid_moves(state)
        
        if player == PLAYER_ID:
            best_score = np.inf
            for move in all_moves:
                state[move[0], move[1]] = player
                evaluated = self.minimax(state, depth-1, BOT_ID)[0]
                state[move[0], move[1]] = 0
                if evaluated < best_score:
                    best_score = evaluated
                    best_move = move
        else:
            best_score = -np.inf
            for move in all_moves:
                state[move[0], move[1]] = player
                evaluated = self.minimax(state, depth-1, PLAYER_ID)[0]
                state[move[0], move[1]] = 0
                if evaluated > best_score:
                    best_score = evaluated
                    best_move = move

        return (best_score, best_move)
    
    def bot_turn(self):
        """
        Searches for the best move and then applies it
        """
        depth = len(self.get_valid_moves(self.board))
        if depth == 9:
            x = np.random.randint(0, self.size)
            y = np.random.randint(0, self.size)
        else:
            _, [x, y] = self.minimax(self.board, depth, BOT_ID)
        
        self.make_move([x, y], BOT_ID)
    
    def run(self):
        """
        Runs the game
        """
        while not(self.is_over(self.board))[1]:
            self.bot_turn()
            print(self.board)
            while True:
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