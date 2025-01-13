# Game Over Screen
def game_over_screen():
    font = pygame.font.SysFont(None, 55)
    message = font.render("Game Over! Press any key to exit.", True, red)
    screen.fill(black)
    screen.blit(message, (width // 4, height // 3))
    pygame.display.update()

    # Wait for the player to press a key or quit
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN:
                waiting = False

# Main game loop
def game_loop():
    game_over = False
    x, y = width // 2, height // 2  # Snake starting position
    x_change, y_change = 0, 0

    snake = [(x, y)]  # Snake body (list of coordinates)
    food = (random.randrange(0, width, block_size), random.randrange(0, height, block_size))

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x_change, y_change = 0, -block_size
                elif event.key == pygame.K_DOWN:
                    x_change, y_change = 0, block_size
                elif event.key == pygame.K_LEFT:
                    x_change, y_change = -block_size, 0
                elif event.key == pygame.K_RIGHT:
                    x_change, y_change = block_size, 0

        # Move snake
        x += x_change
        y += y_change
        snake.append((x, y))

        # Check for collisions
        if x < 0 or x >= width or y < 0 or y >= height or (x, y) in snake[:-1]:
            game_over = True

        # Check if the snake eats food
        if (x, y) == food:
            food = (random.randrange(0, width, block_size), random.randrange(0, height, block_size))
        else:
            snake.pop(0)

        # Drawing
        screen.fill(black)
        pygame.draw.rect(screen, green, (*food, block_size, block_size))
        for segment in snake:
            pygame.draw.rect(screen, blue, (*segment, block_size, block_size))

        pygame.display.update()
        clock.tick(snake_speed)

    game_over_screen()
    pygame.quit()
