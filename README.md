# Introduction
A personal project of a TicTacToe game with implemented Minimax algorithm.

# How it works?
To win in a TicTacToe game, any row/column/diagonal of a 2D board has to be fully filled with only one sign ('O' or 'X'). Computer and player make moves until one of them wins (or until there's a draw).
Computer makes its move based on a Minimax algorithm that recursively analyzes all possible moves and picks the one with the highest value. Computer moves have three values - 0 (if there's a draw), 1 (if it wins), -1 (if the player wins).

# Requirement:
- NumPy

# TODO:
- GUI
- optimize the game for bigger boards (maybe use the depth limit)
