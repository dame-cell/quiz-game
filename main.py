import pygame
import random

pygame.init()

# Set up the display
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up the variables
snake_x = width/2
snake_y = height/2
snake_size = 10
food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
score = 0
font = pygame.font.SysFont(None, 25)
snake_body = []

# Set up the game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x -= snake_size
            elif event.key == pygame.K_RIGHT:
                snake_x += snake_size
            elif event.key == pygame.K_UP:
                snake_y -= snake_size
            elif event.key == pygame.K_DOWN:
                snake_y += snake_size


                # Set up the game loop
game_over = False
while not game_over:
    # Handle events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x -= snake_size
    elif keys[pygame.K_RIGHT]:
        snake_x += snake_size
    elif keys[pygame.K_UP]:
        snake_y -= snake_size
    elif keys[pygame.K_DOWN]:
        snake_y += snake_size

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Check for collision with the food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
        score += 1
        # Add a new body part to the snake
        snake_body.append([snake_x, snake_y])

    # Move the snake's body parts
    if len(snake_body) > 0:
        snake_body = [[snake_x, snake_y]] + snake_body[:-1]

    # Draw the screen
    screen.fill(black)
    for part in snake_body:
        pygame.draw.rect(screen, green, [part[0], part[1], snake_size, snake_size])
    # Draw the snake's head
    pygame.draw.rect(screen, white, [snake_x, snake_y, snake_size, snake_size])
    pygame.draw.rect(screen, red, [food_x, food_y, snake_size, snake_size])
    text = font.render('Score: ' + str(score), True, white)
    screen.blit(text, [0, 0])
    pygame.display.update()

    # Check for game over
    if snake_x < 0 or snake_x > width - snake_size or snake_y < 0 or snake_y > height - snake_size:
        game_over = True

    # Set the game's speed
    clock = pygame.time.Clock()
    clock.tick(10)

# Quit the game
pygame.quit()
quit()
