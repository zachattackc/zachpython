# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This is a Python-based Snake game built with pygame. The project consists of a single main file (`intro.py`) that implements the complete game logic including snake movement, food generation, collision detection, and score tracking.

## Commands

### Running the Game
```bash
python intro.py
```

### Python Environment
The project uses a virtual environment located in `venv/`. Activate it with:
```bash
source venv/bin/activate
```

### Dependencies
The only dependency is pygame (version 2.6.1). Install with:
```bash
pip install pygame
```

## Code Architecture
The game is implemented as a single-file application with the following key components:

- **Game Constants**: Display dimensions (600x600), cell size (20x20), and color definitions
- **Game State**: Snake position array, direction vector, food position, and score
- **Main Loop**: Event handling, game logic updates, collision detection, and rendering
- **Controls**: Arrow keys for directional movement with prevention of reverse direction

The game runs at 10 FPS and uses a grid-based coordinate system where the snake and food are positioned on discrete cells.