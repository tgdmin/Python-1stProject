import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Game settings
snake_block = 10
initial_snake_speed = 8  # Increased initial speed
speed_increase = 1

# Fonts
font_title = pygame.font.SysFont(None, 50)
font_credits = pygame.font.SysFont(None, 20)
font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 35)

# High score and player name variables
high_score = 0
high_score_player = "None"

def score_display(score, high_score, high_score_player):
    value = score_font.render("Score: " + str(score), True, blue)
    high_score_text = score_font.render(f"High Score: {high_score} by {high_score_player}", True, blue)
    window.blit(value, [0, 0])
    window.blit(high_score_text, [0, 30])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color, y_displace=0):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3 + y_displace])

def get_player_name():
    player_name = ""
    input_active = True
    
    while input_active:
        window.fill(white)
        
        # Title and credits displayed at the beginning
        title_text = font_title.render("Snake Game", True, blue)
        credits_text = font_credits.render("Made by Do Minh Tuong", True, blue)
        window.blit(title_text, [width / 2 - title_text.get_width() / 2, 10])
        window.blit(credits_text, [10, height - 30])
        
        # Display prompt and player name on the same row
        prompt_text = font_style.render("Enter Your Name:", True, blue)
        window.blit(prompt_text, [width / 4, height / 2])
        name_text = font_style.render(player_name, True, black)
        window.blit(name_text, [width / 4 + prompt_text.get_width() + 10, height / 2])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if player_name == "":  # Default to "Player" if no name is entered
                        player_name = "Player"
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

        pygame.display.update()
    
    return player_name

def game_loop():
    global high_score, high_score_player

    # Get player's name before starting the game
    player_name = get_player_name()

    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = snake_block
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    snake_speed = initial_snake_speed
    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            window.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            score_display(length_of_snake - 1, high_score, high_score_player)
            pygame.display.update()

            # Update high score and player name if current score is greater
            if length_of_snake - 1 > high_score:
                high_score = length_of_snake - 1
                high_score_player = player_name

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                # Ignore opposite directions to prevent reverse direction
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Check for wall collisions
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(white)
        pygame.draw.rect(window, green, [foodx, foody, snake_block, snake_block])
        
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for self-collision
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        score_display(length_of_snake - 1, high_score, high_score_player)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            snake_speed += speed_increase

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
