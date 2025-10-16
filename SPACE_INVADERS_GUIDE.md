# Space Invaders - Phase 1: Setup & Basic Structure

## Step 1: Create the File
Create a new file called `space_invaders.py` in your project directory.

## Step 2: Import Libraries and Initialize Pygame

```python
import pygame
import random

# Initialize pygame
pygame.init()
```

**What this does:**
- `pygame` - The game library we'll use
- `random` - For random behavior later (alien shooting, etc.)
- `pygame.init()` - Must be called before using any pygame features

## Step 3: Set Up the Display

```python
# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
```

**What this does:**
- Creates an 800x600 pixel window
- Sets the window title to "Space Invaders"

## Step 4: Define Colors

```python
# Color definitions (RGB values)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
```

**What this does:**
- Defines colors using RGB (Red, Green, Blue) values
- Each value ranges from 0-255
- We'll use these for the player, aliens, bullets, etc.

## Step 5: Create Game Constants

```python
# Player settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 40
PLAYER_SPEED = 5

# Alien settings
ALIEN_WIDTH = 40
ALIEN_HEIGHT = 30
ALIEN_ROWS = 5
ALIEN_COLS = 11
ALIEN_SPEED = 1

# Bullet settings
BULLET_WIDTH = 5
BULLET_HEIGHT = 15
BULLET_SPEED = 7

# Game settings
FPS = 60
```

**What this does:**
- **Player constants**: Size of your ship and how fast it moves
- **Alien constants**: Size, how many aliens (5x11 grid), movement speed
- **Bullet constants**: Size and speed of bullets
- **FPS**: Frames per second (60 = smooth gameplay)

## Step 6: Set Up the Game Clock

```python
# Create clock for controlling frame rate
clock = pygame.time.Clock()
```

**What this does:**
- Creates a clock object to control game speed
- We'll use this to run the game at 60 FPS

## Step 7: Create the Main Game Loop

```python
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with black
    screen.fill(BLACK)

    # TODO: Game logic will go here

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

# Quit pygame
pygame.quit()
```

**What this does:**
- **Event handling**: Checks if user closes the window
- **screen.fill(BLACK)**: Clears the screen each frame
- **pygame.display.flip()**: Updates the screen with new drawings
- **clock.tick(FPS)**: Ensures game runs at 60 FPS
- **pygame.quit()**: Cleans up when game ends

## Complete Phase 1 Code

Here's everything together:

```python
import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Color definitions (RGB values)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)

# Player settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 40
PLAYER_SPEED = 5

# Alien settings
ALIEN_WIDTH = 40
ALIEN_HEIGHT = 30
ALIEN_ROWS = 5
ALIEN_COLS = 11
ALIEN_SPEED = 1

# Bullet settings
BULLET_WIDTH = 5
BULLET_HEIGHT = 15
BULLET_SPEED = 7

# Game settings
FPS = 60

# Create clock for controlling frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with black
    screen.fill(BLACK)

    # TODO: Game logic will go here

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

# Quit pygame
pygame.quit()
```

## Testing Phase 1

Run the game with:
```bash
python space_invaders.py
```

**Expected result:**
- A black 800x600 window appears
- Window title says "Space Invaders"
- Window stays open until you close it
- No errors in the terminal

## What You Learned

1. How to set up a pygame window
2. How to define game constants (makes code easier to adjust later)
3. The basic game loop structure (event handling → update → draw → repeat)
4. How to control frame rate

## Next Steps

Once Phase 1 is working, you're ready for **Phase 2: Player Ship** where you'll:
- Create the player spaceship
- Make it move left and right
- Keep it from going off screen

---

**Tips:**
- If you get an error about pygame not being installed, run: `pip install pygame`
- Keep this file open while coding - refer back to the constants section often
- The game loop structure (events → update → draw) is used in almost every game!
