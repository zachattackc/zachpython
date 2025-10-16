import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 40
PLAYER_SPEED = 5

ALIEN_WIDTH = 40
ALIEN = HEIGHT = 30
ALIEN_ROWS = 5
ALIEN_COLS = 11
ALIEN_SPEED = 1

BULLET_WIDTH = 5
BULLET_HEIGHT = 15
BULLET_SPEED = 7

FPS = 60

player_x = WIDTH // 2 - PLAYER_WIDTH // 2
player_y = HEIGHT - PLAYER_HEIGHT - 20
player_velocity = 0



clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_velocity = -PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                player_velocity = PLAYER_SPEED

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player_velocity < 0:
                player_velocity = 0
            if event.key == pygame.K_RIGHT and player_velocity > 0:
                player_velocity = 0
player_x += player_velocity
if player_x < 0:
    player_x = 0
if player_x > WIDTH - PLAYER_WIDTH:
    player_x = WIDTH - PLAYER_WIDTH
screen.fill(BLACK)
pygame.display.flip()
clock.tick(FPS)
pygame.quit()