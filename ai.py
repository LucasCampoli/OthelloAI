import copy
from game_rules import *

class AI:
    def __init__(self, color):
        self.player_color = color
        self.opposite_color = CellStates.BLACK if color == CellStates.WHITE else CellStates.WHITE

    def minimax_wrap(self, board, depth):
        self.minimax(board, depth, -float('inf'), float('inf'), True)

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        best_move = None
        if depth == 0 or not get_valid_plays(board, self.player_color if maximizing_player else self.opposite_color):
            return self.utility(board), best_move
        if maximizing_player:
            max_eval = float('-inf')
            for move in get_valid_plays(board, self.player_color):
                temp_board = copy.deepcopy(board)
                make_move(temp_board, move[0], move[1], self.player_color)
                evaluation = self.minimax(temp_board, depth - 1, alpha, beta, False)[0]
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in get_valid_plays(board, self.opposite_color):
                temp_board = copy.deepcopy(board)
                make_move(temp_board, move[0], move[1], self.opposite_color)
                evaluation = self.minimax(temp_board, depth - 1, alpha, beta, True)[0]
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            return min_eval, best_move


    def utility(self, board):
        return 0
