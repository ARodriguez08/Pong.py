import pygame
from pygame.locals import *
from pause import PauseMenu
from score import Score
from difficulty import DifficultySettings

# Pygame Inicializacion
pygame.init()

# Configuracion de la ventana del juego
window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("Ping Pong")

# Configuracion de Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

# Set up the paddles
paddle_width = 10
paddle_height = 60
paddle_speed = 5
paddle1_y = window_height // 2 - paddle_height // 2
paddle2_y = window_height // 2 - paddle_height // 2

# Set up the ball
ball_radius = 10
ball_speed_x = 3
ball_speed_y = 3
ball_x = window_width // 2
ball_y = window_height // 2

# Set up the pause menu
pause_menu = PauseMenu(window_width, window_height)
show_menu = False

# Set up the score
score = Score(36, window_width, window_height)

# Set up difficulty settings
difficulty_settings = DifficultySettings()
game_difficulty = difficulty_settings.get_difficulty_ticks("Normal")  # Default to Normal difficulty

# Configuracion del boton de pausa
button_font = pygame.font.Font(None, 40)
button_text = button_font.render("||", True, WHITE)
button_rect = button_text.get_rect()
button_rect.topleft = (window_width // 2 - button_rect.width // 2, 20)

# Game loop
running = True
clock = pygame.time.Clock()

def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x = window_width // 2
    ball_y = window_height // 2
    ball_speed_x = -ball_speed_x

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == VIDEORESIZE:
            window_width, window_height = event.w, event.h
            window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
            button_rect.topleft = (window_width // 2 - button_rect.width // 2, 20)
        elif event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if not show_menu:
                    show_menu = True
                else:
                    show_menu = False
                    pause_menu.reset_menu()
            elif show_menu:
                menu_selection = pause_menu.handle_event(event)
                if menu_selection == "Play":
                    show_menu = False
                elif menu_selection in ["Facil", "Normal", "Dificil"]:
                    game_difficulty = difficulty_settings.get_difficulty_ticks(menu_selection)
                    show_menu = False
                elif menu_selection == "Salir":
                    running = False
        elif event.type == MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                if not show_menu:
                    show_menu = True
                else:
                    show_menu = False
                    pause_menu.reset_menu()

    if not show_menu:
        # Move the paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1_y > 0:
            paddle1_y -= paddle_speed
        if keys[pygame.K_s] and paddle1_y < window_height - paddle_height:
            paddle1_y += paddle_speed
        if keys[pygame.K_UP] and paddle2_y > 0:
            paddle2_y -= paddle_speed
        if keys[pygame.K_DOWN] and paddle2_y < window_height - paddle_height:
            paddle2_y += paddle_speed

        # Move the ball
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Check for collisions with walls
        if ball_y <= 0 or ball_y >= window_height - ball_radius:
            ball_speed_y = -ball_speed_y

        # Check for collisions with paddles
        if ball_x <= paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
            ball_speed_x = abs(ball_speed_x)
        elif ball_x >= window_width - paddle_width - ball_radius and paddle2_y <= ball_y <= paddle2_y + paddle_height:
            ball_speed_x = -abs(ball_speed_x)

        # Check for scoring
        if ball_x < 0:
            score.increase_player2()
            reset_ball()
        elif ball_x > window_width:
            score.increase_player1()
            reset_ball()

        # Clear the window
        window.fill(BLACK)

        # Draw the paddles
        pygame.draw.rect(window, WHITE, (20, paddle1_y, paddle_width, paddle_height))
        pygame.draw.rect(window, WHITE, (window_width - 20 - paddle_width, paddle2_y, paddle_width, paddle_height))

        # Draw the ball
        pygame.draw.circle(window, WHITE, (ball_x, ball_y), ball_radius)

        # Draw the pause button
        pygame.draw.rect(window, GRAY, button_rect)
        window.blit(button_text, button_rect.topleft)

        # Draw the score
        score.draw(window)

    else:
        # Draw the pause menu
        pause_menu.draw(window)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(game_difficulty)

# Quit the game
pygame.quit()
