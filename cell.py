from enum import Enum


class CellStates(Enum):
    EMPTY = 0
    WHITE = 1
    BLACK = 2

class Cell:
    state = CellStates.EMPTY
    coords = [0, 0]

    def __init__(self, x, y, initial_state):
        self.coords = [x, y]
        self.state = initial_state