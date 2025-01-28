import copy
from game_rules import *
import numpy as np

white_scoring_matrix = np.array([[16.16, -3.03, 0.99, 0.43, 0.63, 1.33, -4.12, 16.16],
                          [-4.12, -1.81, -0.08, -0.27, -0.18, -0.04, -1.81, -3.03],
                          [1.33, -0.04, 0.51, 0.07, -0.04, 0.51, -0.08, 0.99],
                          [0.63, -0.18, -0.04, -0.01, -0.01, 0.07, -0.27, 0.43],
                          [0.43, -0.27, 0.07, -0.01, -0.01, -0.04, -0.18, 0.63],
                          [0.99, -0.08, 0.51, -0.04, 0.07, 0.51, -0.04, 1.33],
                          [-3.03, -1.81, -0.04, -0.18, -0.27, -0.08, -1.81, -4.12],
                          [16.16, -4.12, 1.33, 0.63, 0.43, 0.99, -3.03, 16.16],
                  ])
black_scoring_matrix = white_scoring_matrix.transpose()


class AI:
    def __init__(self, color):
        self.player_color = color
        self.opposite_color = CellStates.BLACK if color == CellStates.WHITE else CellStates.WHITE

    def minimax_wrap(self, board, depth):
        best_move = self.minimax(board, depth, -float('inf'), float('inf'), True)
        print(best_move[0])
        return best_move

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        best_move = None
        if depth == 0 or not get_valid_plays(board, self.player_color if maximizing_player else self.opposite_color):
            return self.heuristics(board), best_move
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


    def heuristics(self, board):
        frontier_weight = -0.5
        position_weight = 1.0

        white_frontier_score, black_frontier_score = self.get_frontier_disks_score(board)
        white_position_score, black_position_score = self.get_positions_score(board)

        if self.player_color == CellStates.WHITE:
            frontier_score = frontier_weight * (white_frontier_score - black_frontier_score)
            position_score = position_weight * (white_position_score - black_position_score)
        else:
            frontier_score = frontier_weight * (black_frontier_score - white_frontier_score)
            position_score = position_weight * (black_position_score - white_position_score)

        return frontier_score + position_score

    # Count frontier disks for both players
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