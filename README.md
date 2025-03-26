# Snake-Game

Classic snake game using Python's Turtle graphics library. Navigate the snake to eat food and grow while avoiding walls and self-collision.

## Features

- Classic Snake gameplay mechanics
- Two difficulty levels (easy/hard)
- High score tracking system
- Wall collision detection
- Self-collision detection
- Score display
- Smooth snake movement

## Python Concepts Implemented

- **Object-Oriented Programming**
  - Class inheritance (Snake, Food, and Scoreboard inherit from Turtle)
  - Encapsulation of game elements
  - Object attributes and methods

- **File Handling**
  - Reading/writing high scores to `data.txt`
  - File operations using context managers (`with` statement)
  - Error handling for file operations

- **Event Handling**
  - Keyboard input detection
  - Screen event listeners
  - Game loop management

- **Data Structures**
  - Lists for snake segments
  - Coordinate system for positioning
  - Boolean flags for game state

- **Module Organization**
  - Separate modules for different game components
  - Import management
  - Code modularity

## How to Play

1. Run the game: `python main.py`
2. Choose difficulty level when prompted:
   - Easy: slower snake movement
   - Hard: faster snake movement
3. Control the snake using arrow keys:
   - ↑: Move Up
   - ↓: Move Down
   - ←: Move Left
   - →: Move Right
4. Eat the food to grow and increase your score
5. Avoid hitting the walls and the snake's own tail

## Technical Details

- Screen dimensions: 600x600 pixels
- Game boundaries: ±280 pixels
- Collision detection ranges:
  - Food: 15 pixels
  - Self-collision: 10 pixels
- Movement speed:
  - Easy mode: 0.2 seconds delay
  - Hard mode: 0.1 seconds delay

## Dependencies

- Python 3.x
- Built-in libraries:
  - turtle: Graphics and game display
  - time: Movement control
  - os: File path handling

## File Structure

- `main.py`: Game initialization and main loop
- `snake.py`: Snake class and movement logic
- `food.py`: Food class and placement logic
- `scoreboard.py`: Score tracking and display system
- `data.txt`: High score persistent storage
