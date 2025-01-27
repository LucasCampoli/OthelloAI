import math
import sys
from game_rules import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
LIGHT_GREEN = (0, 180, 0)

# Represents the game as an object
class OthelloGame:

    #Initialize board and variables
    def __init__(self):
        self.is_black = None
        pygame.init()
        self.game_board = self.initialize_board()
        self.white_turn = False
        self.screen = None

    # Aux method
    def initialize_board(self):
        board = []
        for row in range(8):
            board.append([])
            for column in range(8):
                if (row == 3 and column == 3) or (row == 4 and column == 4):
                    board[row].append(Cell(column, row, CellStates.WHITE))
                elif (row == 3 and column == 4) or (row == 4 and column == 3):
                    board[row].append(Cell(column, row, CellStates.BLACK))
                else:
                    board[row].append(Cell(column, row, CellStates.EMPTY))
        return board

    # Screen to choose color
    def choose_color(self):
        screen = pygame.display.set_mode((400, 200))
        pygame.display.set_caption("Choose Your Color")
        font = pygame.font.Font(None, 36)
        black_button = pygame.Rect(50, 100, 120, 50)
        white_button = pygame.Rect(230, 100, 120, 50)

        screen.fill((50, 50, 50))
        text = font.render("Choose your color:", True, WHITE)
        screen.blit(text, (100, 30))
        pygame.draw.rect(screen, BLACK, black_button)
        pygame.draw.rect(screen, WHITE, white_button)

        black_text = font.render("Black", True, WHITE)
        white_text = font.render("White", True, BLACK)
        screen.blit(black_text, black_text.get_rect(center=black_button.center))
        screen.blit(white_text, white_text.get_rect(center=white_button.center))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if black_button.collidepoint(event.pos):
                        self.is_black = True
                        return 'black'
                    elif white_button.collidepoint(event.pos):
                        self.is_black = False
                        return 'white'

            pygame.display.flip()

    def draw_board(self):
        self.screen.fill((50, 50, 50))
        pygame.draw.rect(self.screen, LIGHT_GREEN, pygame.Rect(50, 100, 800, 800))

        # Dibujar la cuadrícula
        for i in range(8):
            for j in range(8):
                pygame.draw.line(self.screen, GREEN, (50, 100 * (i + 1) + 100), (850, 100 * (i + 1) + 100), 2)
                pygame.draw.line(self.screen, GREEN, (100 * (j + 1) + 50, 100), (100 * (j + 1) + 50, 900), 2)

        # Dibujar las piezas
        for row in self.game_board:
            for cell in row:
                if cell.state == CellStates.WHITE:
                    pygame.draw.circle(self.screen, WHITE, (cell.coords[0] * 100 + 100, cell.coords[1] * 100 + 150), 48)
                elif cell.state == CellStates.BLACK:
                    pygame.draw.circle(self.screen, BLACK, (cell.coords[0] * 100 + 100, cell.coords[1] * 100 + 150), 48)

    def handle_click(self, pos):
        x, y = pos
        cell_coords = (math.ceil((x - 50) / 100) - 1, math.ceil((y - 100) / 100) - 1)
        if 0 <= cell_coords[0] < 8 and 0 <= cell_coords[1] < 8:
            valid, valid_directions = is_valid_play(self.game_board, cell_coords[0], cell_coords[1], self.white_turn)
            if valid:
                for direction in valid_directions:
                    change_line(self.game_board, cell_coords[0], cell_coords[1], direction, self.white_turn)
                self.white_turn = not self.white_turn
            else:
                print("Invalid move")

    def run(self):
        # Let the play decide color
        self.choose_color()

        # New window to play the game
        self.screen = pygame.display.set_mode((900, 950))
        pygame.display.set_caption("Othello")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            self.draw_board()

            pygame.display.flip()


if __name__ == "__main__":
    game = OthelloGame()
    game.run()
