Python-1stProject

Description
   - The Snake Game program is an interactive Python game where a player controls a snake that grows longer each time it eats food. The goal is to keep the snake alive by avoiding collisions with the screen borders and its own body while achieving the highest possible score. As the snake consumes more food, its speed increases, making the game progressively more challenging.

Functionality
1. Player Setup:
   - Prompts the player to enter their name on the game screen. If left blank, it defaults to "Player."

2. Gameplay:
   - The player controls the snake using the arrow keys (Up, Down, Left, Right).
   - Movement direction changes based on player input, but reverse directions are blocked to prevent immediate self-collision.
   - The snake grows each time it consumes food, which is placed randomly on the screen.
   - After each food consumption, the snake’s speed increases, making the game harder as the player progresses.

3. Score and High Score Tracking:
   - Displays the player’s current score, which is based on the length of the snake.
   - Updates and displays the highest score achieved across sessions, along with the name of the player who achieved it.

4. Game Over and Restart:
   - The game ends if the snake collides with the screen border or itself.
   - A "Game Over" message appears, with options to quit or restart.
   - If the player’s score exceeds the previous high score, it updates the high score record.

5. Graphics and Animations:
   - Smooth animations for snake movement, with dynamically increasing speed.
   - Real-time updates of the score and high score on the game screen.

Achitecture
1. Initialization & Setup
   - Initializes Pygame, sets up display, colors, fonts, and game settings (snake size, speed, screen dimensions).
   - Defines constants for easy tuning.

2. Game Functions
   - score_display(): Shows current score and high score with player names.
   - our_snake(): Renders the snake’s blocks on screen.
   - message(): Displays in-game messages (e.g., "Game Over").
   - get_player_name(): Gets and displays player name input. Defaults to "Player" if blank.

3. Main Game Loop (game_loop())
   - State Management: Runs until the player quits or loses. Includes:
   - Running State: Manages snake movement, detects collisions, spawns food, increases speed, updates score.
   - Game Over State: Allows replay or quit after a collision.
   - Logic & Input Handling: Detects player inputs to move the snake and ignores reverse direction inputs. Collision with the screen or itself triggers game-over.
   - Rendering: Continuously updates visuals, including snake, food, and scores.
   - Speed Control: Uses pygame.time.Clock() to set frame rate based on snake speed.

4. End State
   - Checks if the player has achieved a new high score, updates if so.
   - Ends gracefully with pygame.quit() when the player exits.