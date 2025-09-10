import pygame
import sys
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20
CELLS_X = WIDTH // CELL_SIZE
CELLS_Y = HEIGHT // CELL_SIZE

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

snake = [(CELLS_X // 2, CELLS_Y // 2)]
direction = (1, 0)
food = (random.randint(0, CELLS_X - 1), random.randint(0, CELLS_Y - 1))
score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    
    if (new_head[0] < 0 or new_head[0] >= CELLS_X or 
        new_head[1] < 0 or new_head[1] >= CELLS_Y or 
        new_head in snake):
        print("Game Over! Final Score:", score)
        running = False
        continue
    
    snake.insert(0, new_head)
    
    if new_head == food:
        score += 1
        food = (random.randint(0, CELLS_X - 1), random.randint(0, CELLS_Y - 1))
        while food in snake:
            food = (random.randint(0, CELLS_X - 1), random.randint(0, CELLS_Y - 1))
    else:
        snake.pop()
    
    screen.fill(BLACK)
    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, 
                        (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, 
                         CELL_SIZE, CELL_SIZE))
    
    pygame.draw.rect(screen, RED, 
                    (food[0] * CELL_SIZE, food[1] * CELL_SIZE, 
                     CELL_SIZE, CELL_SIZE))
    
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()




