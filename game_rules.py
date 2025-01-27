from cell import *


def is_valid_play(board, x, y, current_color):
    if board[y][x].state != CellStates.EMPTY:
        return False  # The cell must be empty to be a valid play.

    opponent_color = CellStates.BLACK if current_color == CellStates.WHITE else CellStates.WHITE

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    valid_directions = []
    valid_play = False

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        found_opponent = False

        # Step in the current direction until hitting the edge or breaking the rule.
        while 0 <= nx < 8 and 0 <= ny < 8:
            if board[ny][nx].state == CellStates.EMPTY:
                break  # Empty space means the line is invalid.
            if board[ny][nx].state == current_color:
                if found_opponent:
                    valid_play = True  # Valid line found.
                    valid_directions.append((dx, dy))
                break  # Same color with no opponent in between.
            if board[ny][nx].state == opponent_color:
                found_opponent = True  # Mark that we've seen at least one opponent piece.

            # Move to the next cell in the current direction.
            nx += dx
            ny += dy

    return valid_play, valid_directions  # Return all valid lines.

def get_valid_plays(board, current_color):
    valid_moves = []
    for row in range(8):
        for col in range(8):
            valid_play, valid_directions = is_valid_play(board, col, row, current_color)
            if valid_play:
                valid_moves.append(((col, row), valid_directions))
    return valid_moves


def change_line(board, x, y, direction, current_color):
    nx, ny = x, y
    board[ny][nx].state = current_color

    # Step in the current direction until hitting the edge or finding empty space.
    while 0 <= nx < 8 and 0 <= ny < 8:
        if board[ny][nx].state == CellStates.EMPTY:
            break

        board[ny][nx].state = current_color

        # Move to the next cell in the current direction.
        nx += direction[0]
        ny += direction[1]
