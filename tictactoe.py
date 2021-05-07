"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x = 0
    num_o = 0

    # Counts the number of X and O
    for row in board:
        for cell in row:
            if cell == X:
                num_x += 1
            elif cell == O:
                num_o += 1
    
    # Chooses X or O turn
    if num_x > num_o:
        return O
    else:
        return X   


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Initialize set of possible actions
    possible_actions = set()

    # Checks empty cells in board
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] is None:
                possible_actions.add((i, j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Checks if the action can be done
    if board[action[0]][action[1]] is not None:
        raise Exception("Space taken, choose another space")
    
    # Creates a deepcopy of board
    board_copy = copy.deepcopy(board)

    # Indicate which player's turn
    turn = player(board)

    # Input change in board copy
    board_copy[action[0]][action[1]] = turn

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check Horizontal
    for row in board:
        if row == [X,X,X]:
            return X
        elif row == [O,O,O]:
            return O
    
    # Check Vertical
    for i in range(3):
        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
        elif board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O

    # Check Diagonal
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[2][0] == X and board[1][1] == X and board[0][2] == X:
        return X
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    elif board[2][0] == O and board[1][1] == O and board[0][2] == O:
        return O
    # Returns None if no winner found
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If no winner yet, check if all boxes are full
    if not winner(board):
        n = 0

        for row in board:
            for cell in row:
                if cell != None:
                    n += 1

        if n == 9:
            return True
        else:
            return False

    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    else:
        turn = player(board)

        if turn == X:
            bestVal = -99
            bestmove = None
            for action in actions(board):
                value = min_value(result(board,action))
                if value > bestVal:
                    bestVal = value
                    bestmove = action
            return bestmove
                
        else:
            bestVal = 99
            bestmove = None
            for action in actions(board):
                value = max_value(result(board,action))
                if value < bestVal:
                    bestVal = value
                    bestmove = action
            return bestmove

def max_value(board):
    if terminal(board):
        return utility(board)
    bestVal = -99
    for action in actions(board):
        value = min_value(result(board,action))
        bestVal = max(bestVal,value)
    return bestVal

def min_value(board):
    if terminal(board):
        return utility(board)
    bestVal = 99
    for action in actions(board):
        value = max_value(result(board,action))
        bestVal = min(bestVal, value)
    return bestVal
