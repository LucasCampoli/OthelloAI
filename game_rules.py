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

def get_valid_plays(board, color):
    valid_moves = []
    for row in range(8):
        for col in range(8):
            if is_valid_play(board, col, row, color):
                valid_moves.append((col, row))
    return valid_moves



