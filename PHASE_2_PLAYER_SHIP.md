# Space Invaders - Phase 2: Player Ship

## Overview
In this phase, you'll create the player's spaceship, make it move left and right using arrow keys, and prevent it from going off the screen edges.

## Prerequisites
- Complete Phase 1 (basic game structure running)
- Have `space_invaders.py` open and ready to edit

---

## Step 1: Create Player Variables

Add these lines **after your constants** (after `FPS = 60`) and **before the game loop**:

```python
# Player position (start at bottom center of screen)
player_x = WIDTH // 2 - PLAYER_WIDTH // 2
player_y = HEIGHT - PLAYER_HEIGHT - 20

# Player velocity (how fast it's currently moving)
player_velocity = 0
```

**What this does:**
- `player_x`: Horizontal position (starts in center: WIDTH // 2)
- `player_y`: Vertical position (near bottom: HEIGHT - PLAYER_HEIGHT - 20)
- `player_velocity`: Current speed (-PLAYER_SPEED, 0, or +PLAYER_SPEED)
- The `// 2` centers the player by dividing screen width in half

**Visual explanation:**
```
Screen coordinates:
(0,0) ──────────────────── (800,0)
  │                            │
  │         Game Area          │
  │                            │
  │          [SHIP]  ← player here (centered, near bottom)
(0,600) ──────────────────(800,600)
```

---

## Step 2: Handle Keyboard Input

**Replace** the event handling section in your game loop. Change this:

```python
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```

**To this:**

```python
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_velocity = -PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                player_velocity = PLAYER_SPEED

        # Key released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player_velocity < 0:
                player_velocity = 0
            if event.key == pygame.K_RIGHT and player_velocity > 0:
                player_velocity = 0
```

**What this does:**
- `KEYDOWN`: When you press a key, start moving
- `KEYUP`: When you release a key, stop moving
- Checks which key was pressed (LEFT or RIGHT arrow)
- Sets velocity to negative (left) or positive (right) or zero (stopped)

**Why KEYDOWN and KEYUP?**
- KEYDOWN makes the ship start moving
- KEYUP makes the ship stop when you release the key
- This gives smooth, responsive controls

---

## Step 3: Update Player Position

Add these lines **after the event loop** and **before `screen.fill(BLACK)`**:

```python
    # Update player position
    player_x += player_velocity

    # Keep player on screen (boundary checking)
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - PLAYER_WIDTH:
        player_x = WIDTH - PLAYER_WIDTH
```

**What this does:**
- `player_x += player_velocity`: Moves the player based on current velocity
- **Boundary checking**: Prevents player from going off screen edges
  - If `player_x < 0`: Hit left edge, snap back to 0
  - If `player_x > WIDTH - PLAYER_WIDTH`: Hit right edge, snap back

**Why `WIDTH - PLAYER_WIDTH`?**
- The player is 50 pixels wide
- Screen is 800 pixels wide
- If player_x = 800, the ship would be completely off screen
- So maximum x position = 800 - 50 = 750

---

## Step 4: Draw the Player

Add these lines **after `screen.fill(BLACK)`** in the `# TODO: Game logic will go here` section:

```python
    # Draw player ship
    pygame.draw.rect(screen, GREEN, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    # Optional: Draw a "cockpit" detail on the ship
    pygame.draw.polygon(screen, WHITE, [
        (player_x + PLAYER_WIDTH // 2, player_y),  # Top center point
        (player_x + 10, player_y + PLAYER_HEIGHT), # Bottom left
        (player_x + PLAYER_WIDTH - 10, player_y + PLAYER_HEIGHT) # Bottom right
    ])
```

**What this does:**
- `pygame.draw.rect()`: Draws the main body of the ship (green rectangle)
- Parameters: (screen, color, (x, y, width, height))
- `pygame.draw.polygon()`: Draws a triangle "cockpit" on top (optional but looks cool!)
- The polygon uses three points to create a triangle shape

**Visual result:**
```
    /\      ← White triangle (cockpit)
   /  \
  [====]    ← Green rectangle (ship body)
```

---

## Complete Phase 2 Code

Your game loop section should now look like this:

```python
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_velocity = -PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                player_velocity = PLAYER_SPEED

        # Key released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player_velocity < 0:
                player_velocity = 0
            if event.key == pygame.K_RIGHT and player_velocity > 0:
                player_velocity = 0

    # Update player position
    player_x += player_velocity

    # Keep player on screen (boundary checking)
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - PLAYER_WIDTH:
        player_x = WIDTH - PLAYER_WIDTH

    # Fill screen with black
    screen.fill(BLACK)

    # Draw player ship
    pygame.draw.rect(screen, GREEN, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    # Optional: Draw a "cockpit" detail on the ship
    pygame.draw.polygon(screen, WHITE, [
        (player_x + PLAYER_WIDTH // 2, player_y),
        (player_x + 10, player_y + PLAYER_HEIGHT),
        (player_x + PLAYER_WIDTH - 10, player_y + PLAYER_HEIGHT)
    ])

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

# Quit pygame
pygame.quit()
```

---

## Testing Phase 2

Run the game:
```bash
python space_invaders.py
```

**Expected results:**
1. Green spaceship appears at bottom center of screen
2. Press **LEFT arrow** → ship moves left
3. Press **RIGHT arrow** → ship moves right
4. Release keys → ship stops moving
5. Ship cannot move off the screen edges
6. White triangle "cockpit" on top of the ship (if you added it)

**Troubleshooting:**

| Problem | Solution |
|---------|----------|
| Ship doesn't appear | Check that drawing code is AFTER `screen.fill(BLACK)` |
| Ship won't move | Check you added the player_velocity variable before the loop |
| Ship goes off screen | Check boundary code is BEFORE drawing |
| Ship doesn't stop when key released | Check KEYUP event handling |

---

## What You Learned

1. **Event-driven input**: Using KEYDOWN and KEYUP events
2. **Velocity-based movement**: Using a velocity variable to control speed
3. **Boundary collision**: Keeping objects on screen with if statements
4. **Drawing shapes**: Using `pygame.draw.rect()` and `pygame.draw.polygon()`
5. **Coordinate math**: Understanding x/y positioning and centering

---

## Experimentation Ideas

Try modifying these values to see what happens:

1. **Change speed**: Modify `PLAYER_SPEED = 5` to 3 (slower) or 10 (faster)
2. **Change color**: Replace `GREEN` with `BLUE` or `RED`
3. **Change size**: Modify `PLAYER_WIDTH` and `PLAYER_HEIGHT`
4. **Add more details**: Draw circles for engines using `pygame.draw.circle()`

Example - add engine flames:
```python
# Draw red circles as engines
pygame.draw.circle(screen, RED, (player_x + 10, player_y + PLAYER_HEIGHT), 5)
pygame.draw.circle(screen, RED, (player_x + PLAYER_WIDTH - 10, player_y + PLAYER_HEIGHT), 5)
```

---

## Next Steps

Once Phase 2 is working perfectly, you're ready for **Phase 3: Shooting Mechanics** where you'll:
- Create bullets when spacebar is pressed
- Make bullets move up the screen
- Handle multiple bullets at once
- Remove bullets when they go off screen

---

## Key Concepts Review

**Event Loop Pattern:**
```
Check for input → Update positions → Check boundaries → Draw everything → Repeat
```

**Movement Pattern:**
```
Input changes velocity → Velocity changes position → Position determines where to draw
```

This pattern is used in almost every game, so understanding it now will help you forever!

---

**Great job!** You now have a controllable spaceship. The game is starting to feel interactive! 🚀
