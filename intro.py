import pygame
import sys
import random
pygame.init()

WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20
direction_x = 1
direction_y = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Color Block Bouncer")
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

blockColor = GREEN

rect_x = WIDTH // 2 - CELL_SIZE // 2 #middle of the screen
rect_y = HEIGHT // 2 - CELL_SIZE // 2 #middle of the screen




clock = pygame.time.Clock()
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rect_x += direction_x * CELL_SIZE
    rect_y += direction_y * CELL_SIZE
    # Check horizontal boundaries
    if rect_x <= 0 or rect_x >= WIDTH - CELL_SIZE:
      direction_x = -direction_x
      blockColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0,255))


    # Check vertical boundaries  
    if rect_y <= 0 or rect_y >= HEIGHT - CELL_SIZE:
      direction_y = -direction_y
      blockColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0,255))
    screen.fill(BLACK)
    pygame.draw.rect(screen, blockColor, (rect_x, rect_y, CELL_SIZE, CELL_SIZE))
    pygame.display.flip() #update the screen
    clock.tick(60) #60 fps
pygame.quit()

