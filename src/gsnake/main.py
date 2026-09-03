# Import required modules
import pygame
import random
from pathlib import Path
from .config import *
from importlib import resources

# Game clock
clock = pygame.time.Clock()

# Initialize game variables
def init_game():
    pygame.init()
    pygame.mixer.init()

    game_window = pygame.display.set_mode((width, height))

    bg_asset = resources.files("gsnake").joinpath("assets/images/bg.jpg")
    with resources.as_file(bg_asset) as bg_path:
        background = pygame.image.load(str(bg_path)).convert()
        background = pygame.transform.scale(background, (width, height))
    
    
    color = (255,255,255)
    game_window.fill(color)

    score_font = pygame.font.SysFont(None, 40)
    status_font = pygame.font.SysFont(None, 30)

    pygame.display.set_caption("Feed the Snake")
    pygame.display.update()

    return game_window, score_font, status_font, background

# Display text on screen
def text_screen(game_window, text, font, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])

# Plotting snake on screen
def plot_snake(game_window, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

# Instance of the game
def gameloop(game_window, score_font, status_font, background):
    # game state
    exit_game = False
    game_over = False
    pause = False

    # snake speed
    vel_x = 0
    vel_y = 0
    thrust = 0

    # snake position
    snake_x = 340
    snake_y = 55

    # snake dimensions
    snake_size = 20
    snake_list = []
    snake_length = 1

    # food and score
    food_x = random.randint(20, width-20)
    food_y = random.randint(20, height-20)
    score = 0

    # music and fps
    global music
    fps = 35

    if music:
        music_asset = resources.files("gsnake").joinpath("assets/sounds/music.mp3")
        pygame.mixer.music.load(music_asset)
        pygame.mixer.music.play()

    while not exit_game:
        if game_over:
            game_window.fill(black)
            text_screen(game_window, 'Game Over',
                        score_font, red, width-650, height-400)
            text_screen(game_window, 'Press enter to continue',
                        score_font, red, width-730, height-360)
            music = False
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop(game_window, score_font, status_font, background)

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True
                    if event.key == pygame.K_RIGHT:
                        vel_x = 10 + thrust
                        vel_y = 0
                        pause = False
                    if event.key == pygame.K_LEFT:
                        vel_x = -10 - thrust
                        vel_y = 0
                        pause = False
                    if event.key == pygame.K_UP:
                        vel_y = -10 - thrust
                        vel_x = 0
                        pause = False
                    if event.key == pygame.K_DOWN:
                        vel_y = 10 + thrust
                        vel_x = 0
                        pause = False
                    if event.key == pygame.K_SPACE:
                        vel_x, vel_y = 0, 0
                        pause = True
                    if event.key == pygame.K_w:
                        thrust += 2
                        speed = True
                        tazer = False
                    if event.key == pygame.K_s:
                        speed = False
                        tazer = True
                        thrust += -2

            if abs(snake_x-food_x) < 7 and abs(snake_y-food_y) < 7:
                score += 10
                food_x = random.randint(20, width-20)
                food_y = random.randint(20, height-20)
                snake_length += 1
            
            # Snake teleporting
            if snake_x > (width - 10):
                snake_x = 10
            elif snake_x < 5:
                snake_x = width - 10
            elif snake_y > (height - 10):
                snake_y = 10
            elif snake_y < 10:
                snake_y = height - 10

            game_window.blit(background, (0, 0))

            if pause:
                text_screen(game_window, 'Paused...',
                            score_font, green, 600-70, 300)

            text_screen(game_window, f'Speed: {abs(vel_x + vel_y)}',
                        score_font, black, 10, 50)
            text_screen(
                game_window, f'Score: {str(score)}', score_font, red, 10, 10)
            text_screen(game_window, "Licensed under GNU GPLv3 by rookie2373", status_font,
                        black, width-850, height-25)

            pygame.draw.rect(game_window, blue, [0, 0, 5, height])
            pygame.draw.rect(game_window, blue, [0, 0, width, 5])
            pygame.draw.rect(game_window, blue, [0, height-5, width, 5])
            pygame.draw.rect(game_window, blue, [width-5, 0, 5, height])
            pygame.draw.rect(game_window, red, [
                             food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
            plot_snake(game_window, black, snake_list, snake_size)
            snake_x += vel_x
            snake_y += vel_y

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

# Start of application
def main():
    gw, scfont, stfont, background = init_game()
    gameloop(game_window=gw, score_font=scfont, status_font=stfont, background=background)
