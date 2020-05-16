from game_state import Game_state
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import pygame

Screen_Width = 640
Screen_Height = 320

Color_White = (255, 255, 255)
Color_Black = (0, 0, 0)
Color_Red = (255, 0, 0)
Color_Green = (0, 255, 0)
Color_Blue = (0, 0, 255)

gs = Game_state()
num_of_player = gs.num_of_player

pygame.init()  # 啟動 Pygame
screen = pygame.display.set_mode((640, 320))  # 建立繪圖視窗
pygame.display.set_caption("基本架構")  # 繪圖視窗標題

background = pygame.Surface(screen.get_size())  # 建立畫布
background = background.convert()
background.fill(Color_White)  # 畫布為白色

step_size = 10
snake_length = 10

snakes = [Snake(step_size, snake_length, i, background) for i in range(num_of_player)]

screen.blit(background, (0, 0))  # 在繪圖視窗繪製畫布
pygame.display.update()  # 更新繪圖視窗

food = Food(step_size, background)

scoreboard = Scoreboard(screen, snakes)

clock = pygame.time.Clock()  # 建立時間元件

running = True
while running:  # 無窮迴圈

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 使用者按關閉鈕
            running = False

        elif event.type == pygame.KEYDOWN:
            for i in range(num_of_player):
                if event.key in snakes[i].pyKey_to_direct:
                    snakes[i].direct = snakes[i].pyKey_to_direct[event.key]
    if not running:
        break

    for i, snake in enumerate(snakes):
        running = snake.move()
        if not running:
            break

    for i in range(num_of_player):
        curr_snake = snakes[i]

        if curr_snake.inevitable:
            continue

        for j in range(num_of_player):
            if i == j:
                continue
            other_snake = snakes[j]

            if tuple(curr_snake.head) in other_snake.visited:
                curr_snake.is_valid = False
                running = False

    fx, fy = food.pos
    food.show()

    for snake in snakes:
        if snake.head == food.pos:

            if food.inevitable:
                snake.inevitable = True
                snake.inevitable_cnt = 0

            snake.gorw()
            food.create()

        snake.show()

    screen.blit(background, (0, 0))  # 在繪圖視窗繪製畫布

    # 更新計分板
    scoreboard.update()

    pygame.display.update()  # 更新繪圖視窗

    # time.sleep(0.1)
    clock.tick(10)

pygame.quit()  # 關閉繪圖視窗

gs.show_winner(snakes)
