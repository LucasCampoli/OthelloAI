from enum import Enum

import pygame


class CellStates(Enum):
    EMPTY = 0
    WHITE = 1
    BLACK = -1

class Cell:
    def __init__(self, x, y, initial_state):
        self.coords = [x, y]
        self.state = initial_state
        self.collider = pygame.Rect(100*x + 51, 100*y + 101, 99, 99)