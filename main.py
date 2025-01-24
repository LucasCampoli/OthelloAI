import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
LIGHT_GREEN = (0, 180, 0)

def choose_color():
    # Initialize pygame and draw
    pygame.init()
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

if __name__ == "__main__":
    player_color = choose_color()

