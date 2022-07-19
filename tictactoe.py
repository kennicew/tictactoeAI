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
    x_count = 0
    o_count = 0

    for i in board:
        for j in i:
            if j == X:
                x_count += 1
            elif j == O:
                o_count += 1
    
    if x_count > o_count:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                square = (i, j)
                actions.add(square)

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
         raise ValueError

    board_copy = copy.deepcopy(board)
    i, j = action
    board_copy[i][j] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # 3x horizontal, 3x vertical, 2x diagonal
    for i in range(3):
        if board[i][0] != EMPTY:
            winner = board[i][0]
            if winner == board[i][1] and winner == board[i][2]:
                return winner
    
    for i in range(3):
        if board[0][i] != EMPTY:
            winner = board[0][i]
            if winner == board[1][i] and winner == board[2][i]:
                return winner
    
    if board[1][1] != EMPTY:
        winner = board[1][1]
        if winner == board[0][0] and winner == board[2][2]:
            return winner
        if winner == board[0][2] and winner == board[2][0]:
            return winner
    
    return None




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # someone has won the game or because all cells have been filled without anyone winning
    if winner(board) != None or any(EMPTY in x for x in board) == False:
        return True
    return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

# Did not work but don't understand why
# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """

#     best_action = None 
    
#     def maxValue(board):
#         nonlocal best_action
#         v = float('-inf')
#         if terminal(board):
#             return utility(board)
#         for action in actions(board):
#             v_temp = minValue(result(board, action))
#             if v_temp > v:
#                 v = v_temp
#                 best_action = action
#         return v

#     def minValue(board):
#         nonlocal best_action
#         v = float('inf')
#         if terminal(board):
#             return utility(board)
#         for action in actions(board):
#             v_temp = maxValue(result(board, action))
#             if v_temp < v:
#                 v = v_temp
#                 best_action = action
#         return v

#     if terminal(board):
#         return None
#     if player(board) == X:
#         maxValue(board)
#     else:
#         minValue(board)

#     return best_action
        
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """ 
    def maxValue(board):
        v = float('-inf')
        if terminal(board):
            return utility(board), None
        for action in actions(board):
            v_temp, a = minValue(result(board, action))
            if v_temp > v:
                v = v_temp
                best_action = action
                if v == 1:
                    break
        return v, best_action

    def minValue(board):
        v = float('inf')
        if terminal(board):
            return utility(board), None
        for action in actions(board):
            v_temp, a = maxValue(result(board, action))
            if v_temp < v:
                v = v_temp
                best_action = action
                if v == -1:
                     break
        return v, best_action

    if terminal(board):
        return None
    elif player(board) == X:
        v, a = maxValue(board)
        return a
        
    else:
        v, a = minValue(board)
        return a

        