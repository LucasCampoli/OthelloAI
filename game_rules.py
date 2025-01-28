from cell import *


def is_valid_play(board, col, row, color):
    if board[row][col].state != CellStates.EMPTY:
        return False
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    opposite_color = CellStates.BLACK if color == CellStates.WHITE else CellStates.WHITE
    for dr, dc in directions:
        r, c = row + dr, col + dc
        has_opposite = False
        while 0 <= r < 8 and 0 <= c < 8:
            if board[r][c].state == opposite_color:
                has_opposite = True
            elif board[r][c].state == color and has_opposite:
                return True
            else:
                break
            r += dr
            c += dc
    return False

# Count player frontier and opponent frontier
def get_frontier_disks(board, player_color, opponent_color):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    player_frontier = 0
    opponent_frontier = 0

    for i in range(8):
        for j in range(8):
            if board[i][j] == player_color or board[i][j] == opponent_color:
                is_frontier = False
                for di, dj in directions:
                    neighbor_i = i + di
                    neighbor_j = j + dj
                    if 0 <= neighbor_i < 8 and 0 <= neighbor_j < 8:
                        if board[neighbor_i][neighbor_j] == 0:
                            is_frontier = True
                            break

                if is_frontier:
                    if board[i][j] == player_color:
                        player_frontier += 1
                    else:
                        opponent_frontier += 1
    return player_frontier, opponent_frontier


def get_valid_plays(board, color):
    valid_moves = []
    for row in range(8):
        for col in range(8):
            if is_valid_play(board, col, row, color):
                valid_moves.append((col, row))
    return valid_moves

def make_move(board, col, row, color):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    board[row][col].state = color
    opponent_color = (CellStates.WHITE if color == CellStates.BLACK else CellStates.BLACK)
    for dr, dc in directions:
        r, c = row + dr, col + dc
        to_flip = []
        while 0 <= r < 8 and 0 <= c < 8:
            if board[r][c].state == opponent_color:
                to_flip.append((r, c))
            elif board[r][c].state == color:
                for flip_r, flip_c in to_flip:
                    board[flip_r][flip_c].state = color
                break
            else:
                break
            r += dr
            c += dc
    return board