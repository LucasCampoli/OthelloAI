from enum import Enum

import pygame
import sys
import cell
from cell import CellStates

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
LIGHT_GREEN = (0, 180, 0)

def choose_color():
    # Initialize draw
    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Choose Your Color")
    font = pygame.font.Font(None, 36)
    black_button = pygame.Rect(50, 100, 120, 50)
    white_button = pygame.Rect(230, 100, 120, 50)

    # Draw screen
    screen.fill((50, 50, 50))

    text = font.render("Choose your color:", True, WHITE)
    screen.blit(text, (100, 30))

    pygame.draw.rect(screen, BLACK, black_button)
    pygame.draw.rect(screen, WHITE, white_button)
    black_text = font.render("Black", True, WHITE)
    white_text = font.render("White", True, BLACK)
    screen.blit(black_text, (70, 110))
    screen.blit(white_text, (250, 110))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if black_button.collidepoint(event.pos):
                    return 'black'
                elif white_button.collidepoint(event.pos):
                    return 'white'

        pygame.display.flip()

def draw_board(board):
    screen.fill(LIGHT_GREEN)

    for i in range(8):
        for j in range (8):
            pygame.draw.line(screen, GREEN, (0, 100 * (i+1)), (800, 100 * (i+1)), 2)
            pygame.draw.line(screen, GREEN, (100 * (j+1), 0), (100 * (j+1), 800), 2)

    for row in board:
        for current_cell in row:
            if current_cell.state == CellStates.WHITE:
                #draw white piece
                pygame.draw.circle(screen, WHITE, (current_cell.coords[0] * 100 + 50, current_cell.coords[1] * 100 + 50),48)
            elif current_cell.state == CellStates.BLACK:
                #draw black piece
                pygame.draw.circle(screen, BLACK, (current_cell.coords[0] * 100 + 50, current_cell.coords[1] * 100 + 50),48)


if __name__ == "__main__":
    pygame.init()
    player_color = choose_color()
    screen = pygame.display.set_mode((800, 800))

    game_board = ([cell.Cell(0, 0, CellStates.EMPTY),
                   cell.Cell(1, 0, CellStates.EMPTY),
                   cell.Cell(2, 0, CellStates.EMPTY),
                   cell.Cell(3, 0, CellStates.EMPTY),
                   cell.Cell(4, 0, CellStates.EMPTY),
                   cell.Cell(5, 0, CellStates.EMPTY),
                   cell.Cell(6, 0, CellStates.EMPTY),
                   cell.Cell(7, 0, CellStates.EMPTY)],
                  [cell.Cell(0, 1, CellStates.EMPTY),
                   cell.Cell(1, 1, CellStates.EMPTY),
                   cell.Cell(2, 1, CellStates.EMPTY),
                   cell.Cell(3, 1, CellStates.EMPTY),
                   cell.Cell(4, 1, CellStates.EMPTY),
                   cell.Cell(5, 1, CellStates.EMPTY),
                   cell.Cell(6, 1, CellStates.EMPTY),
                   cell.Cell(7, 1, CellStates.EMPTY)],
                  [cell.Cell(0, 2, CellStates.EMPTY),
                   cell.Cell(1, 2, CellStates.EMPTY),
                   cell.Cell(2, 2, CellStates.EMPTY),
                   cell.Cell(3, 2, CellStates.EMPTY),
                   cell.Cell(4, 2, CellStates.EMPTY),
                   cell.Cell(5, 2, CellStates.EMPTY),
                   cell.Cell(6, 2, CellStates.EMPTY),
                   cell.Cell(7, 2, CellStates.EMPTY)],
                  [cell.Cell(0, 3, CellStates.EMPTY),
                   cell.Cell(1, 3, CellStates.EMPTY),
                   cell.Cell(2, 3, CellStates.EMPTY),
                   cell.Cell(3, 3, CellStates.WHITE),
                   cell.Cell(4, 3, CellStates.BLACK),
                   cell.Cell(5, 3, CellStates.EMPTY),
                   cell.Cell(6, 3, CellStates.EMPTY),
                   cell.Cell(7, 3, CellStates.EMPTY)],
                  [cell.Cell(0, 4, CellStates.EMPTY),
                   cell.Cell(1, 4, CellStates.EMPTY),
                   cell.Cell(2, 4, CellStates.EMPTY),
                   cell.Cell(3, 4, CellStates.BLACK),
                   cell.Cell(4, 4, CellStates.WHITE),
                   cell.Cell(5, 4, CellStates.EMPTY),
                   cell.Cell(6, 4, CellStates.EMPTY),
                   cell.Cell(7, 4, CellStates.EMPTY)],
                  [cell.Cell(0, 5, CellStates.EMPTY),
                   cell.Cell(1, 5, CellStates.EMPTY),
                   cell.Cell(2, 5, CellStates.EMPTY),
                   cell.Cell(3, 5, CellStates.EMPTY),
                   cell.Cell(4, 5, CellStates.EMPTY),
                   cell.Cell(5, 5, CellStates.EMPTY),
                   cell.Cell(6, 5, CellStates.EMPTY),
                   cell.Cell(7, 5, CellStates.EMPTY)],
                  [cell.Cell(0, 6, CellStates.EMPTY),
                   cell.Cell(1, 6, CellStates.EMPTY),
                   cell.Cell(2, 6, CellStates.EMPTY),
                   cell.Cell(3, 6, CellStates.EMPTY),
                   cell.Cell(4, 6, CellStates.EMPTY),
                   cell.Cell(5, 6, CellStates.EMPTY),
                   cell.Cell(6, 6, CellStates.EMPTY),
                   cell.Cell(7, 6, CellStates.EMPTY)],
                  [cell.Cell(0, 7, CellStates.EMPTY),
                   cell.Cell(1, 7, CellStates.EMPTY),
                   cell.Cell(2, 7, CellStates.EMPTY),
                   cell.Cell(3, 7, CellStates.EMPTY),
                   cell.Cell(4, 7, CellStates.EMPTY),
                   cell.Cell(5, 7, CellStates.EMPTY),
                   cell.Cell(6, 7, CellStates.EMPTY),
                   cell.Cell(7, 7, CellStates.EMPTY)])

    while True:
        draw_board(game_board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        continue
