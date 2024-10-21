# Python-1stProject
Snake Game
Description
This project is a simple implementation of the classic Snake Game. The player controls a snake that moves around the screen, eating food to grow longer while avoiding collisions with the walls and its own body. The game ends if the snake collides with itself or the walls.

Functionality
Control the Snake: Use arrow keys to change the snake’s direction.
Eat Food: Snake grows longer when it eats food.
Score: Score increases with each piece of food eaten.
Game Over: The game ends if the snake hits the walls or itself.
Restart or Exit: After the game ends, players can choose to restart or exit.
Architecture
Classes
Snake: Manages the snake’s movement and size.
move(): Moves the snake.
grow(): Increases the snake's length.
check_collision(): Checks for collisions.

Food: Places food randomly on the screen.
new_position(): Generates a new food position.

Game: Handles the main game logic.
run(): Runs the game loop.
reset(): Resets the game after it ends.