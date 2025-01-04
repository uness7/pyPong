import pygame

def loop_game():
    SCREEN_WIDTH: int = 1280
    SCREEN_HEIGHT: int = 800

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    ball = pygame.Rect(0, 0, 30, 30)
    ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    cpu = pygame.Rect(0, 0, 20, 220)
    cpu.centery = (SCREEN_HEIGHT / 2)

    player = pygame.Rect(SCREEN_WIDTH - 20 , 0, 20, 220)
    player.centery = (SCREEN_HEIGHT / 2)

    ball_speed_x = 6
    ball_speed_y = 6

    player_speed_y = 0
    cpy_speed = 6

    out_space_counter = 0
    is_game_finished = False


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_speed_y = -6
                elif event.key == pygame.K_DOWN:
                    player_speed_y = 6
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player_speed_y =0
                elif event.key == pygame.K_DOWN:
                    player_speed_y =0


        ball.x += ball_speed_x
        ball.y += ball_speed_y

        player.y += player_speed_y
        cpu.y += cpy_speed

        if ball.centery <= cpu.centery:
            cpy_speed = -6
        elif ball.centery >= cpu.centery:
            cpy_speed = 6

        if cpu.top <= 0:
                cpu.top = 0
        elif cpu.bottom >= SCREEN_HEIGHT:
            cpu.bottom = SCREEN_HEIGHT

        if ball.right >= SCREEN_WIDTH or ball.left <= 0:
            out_space_counter += 1
            if out_space_counter > 2:
                return

        if ball.bottom >= SCREEN_HEIGHT or ball.top <= 0:
            ball_speed_y *= -1

        if ball.colliderect(player):
            ball_speed_x *= -1

        if ball.colliderect(cpu):
            ball_speed_x *= -1

        if player.bottom >= SCREEN_HEIGHT or player.top <= 0:
            player_speed_y = 0

        screen.fill("black")
        pygame.draw.ellipse(screen, "white", ball)
        pygame.draw.rect(screen, "white", cpu)
        pygame.draw.rect(screen, "white", player)

        # RENDER YOUR GAME HERE

        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
        pygame.quit()

while True:
    loop_game()
