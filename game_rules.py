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


def is_terminal(board):
    if not get_valid_plays(board, CellStates.BLACK) and not get_valid_plays(board, CellStates.WHITE):
        return True
    return False

def winner(board):
    white_score = sum(cell.state == CellStates.WHITE for row in board for cell in row)
    black_score = sum(cell.state == CellStates.BLACK for row in board for cell in row)

    if white_score > black_score:
        return CellStates.WHITE
    elif black_score > white_score:
        return CellStates.BLACK
    else:
        return None

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