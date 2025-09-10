import pygame
import sys
import random   #for random number generation


pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake Game")
running = True
while running:
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
        console.log("Game over")
pygame.quit()
sys.exit() #quits the app when we are done




