import copy

from numpy.ma.core import equal

import game_rules
from game_rules import *
import numpy as np

white_scoring_matrix = np.array([
    [20.0, -3.5, 1.5, 0.5, 0.5, 1.5, -3.5, 20.0],  # Corners emphasized more
    [-3.5, -2.0, -0.5, -0.3, -0.3, -0.5, -2.0, -3.5],  # Edge penalties adjusted
    [1.5, -0.5, 0.7, 0.1, 0.1, 0.7, -0.5, 1.5],  # Inner squares slightly increased
    [0.5, -0.3, 0.1, 0.0, 0.0, 0.1, -0.3, 0.5],  # Center squares neutral
    [0.5, -0.3, 0.1, 0.0, 0.0, 0.1, -0.3, 0.5],  # Center squares neutral
    [1.5, -0.5, 0.7, 0.1, 0.1, 0.7, -0.5, 1.5],  # Inner squares slightly increased
    [-3.5, -2.0, -0.5, -0.3, -0.3, -0.5, -2.0, -3.5],  # Edge penalties adjusted
    [20.0, -3.5, 1.5, 0.5, 0.5, 1.5, -3.5, 20.0],  # Corners emphasized more
])

black_scoring_matrix = white_scoring_matrix.transpose()


class AI:
    def __init__(self, color):
        self.player_color = color
        self.opposite_color = CellStates.BLACK if color == CellStates.WHITE else CellStates.WHITE

    def minimax_wrap(self, board, depth):
        return self.max_player(board, depth, -float('inf'), float('inf'))

    def max_player(self, board, depth, alpha, beta):
        best_move = None

        if game_rules.is_terminal(board) or depth == 0:
            return self.heuristics(board), best_move

        max_eval = float('-inf')
        for move in get_valid_plays(board, self.player_color):
            temp_board = copy.deepcopy(board)
            make_move(temp_board, move[0], move[1], self.player_color)
            evaluation = self.min_player(temp_board, depth - 1, alpha, beta)[0]
            if best_move is None or evaluation > max_eval:
                max_eval = evaluation
                best_move = move

            alpha = max(alpha, evaluation)
            if beta <= evaluation:
                break
        return max_eval, best_move

    def min_player(self, board, depth, alpha, beta):
        best_move = None

        if game_rules.is_terminal(board) or depth == 0:
            return self.heuristics(board), best_move

        min_eval = float('inf')
        for move in get_valid_plays(board, self.opposite_color):
            temp_board = copy.deepcopy(board)
            make_move(temp_board, move[0], move[1], self.opposite_color)
            evaluation = self.max_player(temp_board, depth - 1, alpha, beta)[0]
            if best_move is None or evaluation < min_eval:
                min_eval = evaluation
                best_move = move
            beta = min(beta, evaluation)
            if evaluation <= alpha:
                break
        return min_eval, best_move

    def heuristics(self, board):
        position_weight = 1.2
        frontier_weight = -0.3
        mobility_weight = 0.8

        white_frontier_score, black_frontier_score = self.get_frontier_disks_score(board)
        white_position_score, black_position_score = self.get_positions_score(board)
        white_mobility, black_mobility = self.get_mobility_score(board)
        terminal_score = self.get_terminal_score(board)

        if self.player_color == CellStates.WHITE:
            frontier_score = frontier_weight * (white_frontier_score - black_frontier_score)
            position_score = position_weight * (white_position_score - black_position_score)
            mobility_score = mobility_weight * (white_mobility - black_mobility)
        else:
            frontier_score = frontier_weight * (black_frontier_score - white_frontier_score)
            position_score = position_weight * (black_position_score - white_position_score)
            mobility_score = mobility_weight * (black_mobility - white_mobility)

        return terminal_score if terminal_score != 0 else frontier_score + position_score + mobility_score

    def get_frontier_disks_score(self, board):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        white_frontier = 0
        black_frontier = 0

        for i in range(8):
            for j in range(8):
                if board[i][j] == self.player_color or board[i][j] == self.opposite_color:
                    is_frontier = False
                    for di, dj in directions:
                        neighbor_i = i + di
                        neighbor_j = j + dj
                        if 0 <= neighbor_i < 8 and 0 <= neighbor_j < 8 and board[neighbor_i][neighbor_j].state == CellStates.EMPTY:
                            is_frontier = True
                            break
                    if is_frontier:
                        if board[i][j].state == CellStates.BLACK:
                            black_frontier += 1
                        else:
                            white_frontier += 1
        return white_frontier, black_frontier

    def get_positions_score(self, board):
        white_score = 0
        black_score = 0
        for i in range(8):
            for j in range(8):
                if board[i][j].state == CellStates.WHITE:
                    white_score += white_scoring_matrix[i][j]
                elif board[i][j].state == CellStates.BLACK:
                    black_score += black_scoring_matrix[i][j]
        return white_score, black_score

    def get_mobility_score(self, board):
        white_mobility = len(get_valid_plays(board, CellStates.WHITE))
        black_mobility = len(get_valid_plays(board, CellStates.BLACK))
        return white_mobility, black_mobility

    def get_terminal_score(self, board):
        if game_rules.is_terminal(board):
            player_winner = game_rules.winner(board)
            if player_winner == self.player_color:
                return float('inf')
            else:
                return -float('inf')
        return 0
