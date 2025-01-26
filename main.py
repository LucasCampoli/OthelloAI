import math
from enum import Enum

import pygame
import sys
from cell import *
from game_rules import *

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
    screen.fill((50,50,50))
    pygame.draw.rect(screen, LIGHT_GREEN, pygame.Rect(50, 100, 800, 800))

    for i in range(8):
        for j in range (8):
            pygame.draw.line(screen, GREEN, (50, 100 * (i+1) + 100), (850, 100 * (i+1) + 100), 2)
            pygame.draw.line(screen, GREEN, (100 * (j+1) + 50, 100), (100 * (j+1) + 50, 900), 2)

    for row in board:
        for current_cell in row:
            if current_cell.state == CellStates.WHITE:
                #draw white piece
                pygame.draw.circle(screen, WHITE, (current_cell.coords[0] * 100 + 100, current_cell.coords[1] * 100 + 150),48)
            elif current_cell.state == CellStates.BLACK:
                #draw black piece
                pygame.draw.circle(screen, BLACK, (current_cell.coords[0] * 100 + 100, current_cell.coords[1] * 100 + 150),48)

if __name__ == "__main__":
    pygame.init()
    player_color = choose_color()
    screen = pygame.display.set_mode((900, 950))

    game_board = []
    for row in range(8):
        game_board.append([])
        for column in range(8):
            if (row == 3 and column == 3) or (row == 4 and column == 4):
                game_board[row].append(Cell(column, row, CellStates.WHITE))
            elif (row == 3 and column == 4) or (row == 4 and column == 3):
                game_board[row].append(Cell(column, row, CellStates.BLACK))
            else:
                game_board[row].append(Cell(column, row, CellStates.EMPTY))

    white_turn = False

    while True:
        draw_board(game_board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                cell_coords = (math.ceil((x - 50) / 100) - 1, math.ceil((y - 100) / 100) - 1)
                if not (cell_coords[0] < 0 or cell_coords[0] >= 8 or cell_coords[1] < 0 or cell_coords[1] >= 8):
                    valid, valid_directions = is_valid_play(game_board, cell_coords[0], cell_coords[1], white_turn)
                    if valid:
                        for direction in valid_directions:
                            change_line(game_board, cell_coords[0], cell_coords[1], direction, white_turn)
                        white_turn = not white_turn
                    else:
                        print('invalid play')

        pygame.display.flip()
