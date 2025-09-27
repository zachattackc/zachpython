import pygame
import random
pygame.init()

WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20
# Randomize starting direction with any angle
# random.uniform gives a random float between -1 and 1
# This allows the square to move in any direction, not just diagonal
direction_x = random.uniform(-1, 1)
direction_y = random.uniform(-1, 1)

# Make sure it's not standing still (very unlikely but possible if both are near 0)
while abs(direction_x) < 0.1 and abs(direction_y) < 0.1:
    direction_x = random.uniform(-1, 1)
    direction_y = random.uniform(-1, 1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Image Generator")
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

# Trail storage - this list will store tuples of (x, y, color) for each trail segment
# No maximum length - the trail will keep growing forever!
trail = []




clock = pygame.time.Clock()
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Before moving, add current position and color to the trail
    trail.append((rect_x, rect_y, blockColor))

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

    # Draw the trail - loop through all saved positions and draw them
    for trail_x, trail_y, trail_color in trail:
        pygame.draw.rect(screen, trail_color, (trail_x, trail_y, CELL_SIZE, CELL_SIZE))

    # Draw the main square (on top of the trail)
    pygame.draw.rect(screen, blockColor, (rect_x, rect_y, CELL_SIZE, CELL_SIZE))
    pygame.display.flip() #update the screen
    clock.tick(120) #60 fps
pygame.quit()

