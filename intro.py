import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake Game - Step 1")
("black") (0, 0, 0)
pygame.timeclock()
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
screen.fill("black")
pygame.display.flip()
clock.tick(60)
pygame.quit()

