import pygame
import sys
pygame.init()

WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Step 1")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)
CYAN = (0, 255, 255)
PINK = (255, 192, 203)

clock = pygame.time.Clock()
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill(BLACK)
        rect_x = WIDTH // 2 - CELL_SIZE // 2
        rect_y = HEIGHT // 2 - CELL_SIZE // 2
        pygame.draw.rect(screen, GREEN, (rect_x, rect_y, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
    clock.tick(60)
pygame.quit()

