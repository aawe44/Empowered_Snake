import pygame
import time

Color_White = (255, 255, 255)


class Game_state:
    def __init__(self):

        self.num_of_player = self.select_num_of_player()

    def select_num_of_player(self):

        pygame.init()  # 啟動 Pygame
        screen = pygame.display.set_mode((640, 320))  # 建立繪圖視窗
        pygame.display.set_caption("基本架構")  # 繪圖視窗標題

        background = pygame.Surface(screen.get_size())  # 建立畫布
        background = background.convert()
        background.fill(Color_White)  # 畫布為白色

        strings = ["Number of player, press space to select.", "=> one player", "two players"]

        running = True

        cnt = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 使用者按關閉鈕
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        cnt += 1

                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE:
                        running = False

            idx = cnt % 2

            strings[1] = "=> one player" if idx == 0 else "    one player"
            strings[2] = "    two players" if idx == 0 else "=> two players"

            screen.blit(background, (0, 0))  # 在繪圖視窗繪製畫布

            for i, string in enumerate(strings):
                font = pygame.font.SysFont("comicsansms", 16)
                text = font.render(string, True, (0, 0, 255), Color_White)  # 綠色底，藍色字 (R,G,B)
                screen.blit(text, (250, 100 + 20 * i))

            pygame.display.update()  # 更新繪圖視窗
            time.sleep(0.1)

        screen.blit(background, (0, 0))  # 在繪圖視窗繪製畫布

        num_of_player = cnt % 2 + 1

        string = "one player" if num_of_player == 1 else "two players"
        font = pygame.font.SysFont("comicsansms", 24)
        text = font.render(string, True, (0, 0, 255), Color_White)  # 綠色底，藍色字 (R,G,B)
        screen.blit(text, (250, 100))
        pygame.display.update()
        time.sleep(3)

        pygame.quit()  # 關閉繪圖視窗
        return num_of_player

    def show_winner(self, snakes):

        pygame.init()  # 啟動 Pygame
        screen = pygame.display.set_mode((640, 320))  # 建立繪圖視窗
        pygame.display.set_caption("基本架構")  # 繪圖視窗標題

        background = pygame.Surface(screen.get_size())  # 建立畫布
        background = background.convert()
        background.fill(Color_White)  # 畫布為白色
        screen.blit(background, (0, 0))  # 在繪圖視窗繪製畫布

        if len(snakes) == 1:
            string = "Game Over"

        else:
            string = "Winner is player "
            for snake in snakes:
                if snake.is_valid:
                    string += str(snake.player + 1)

        font = pygame.font.SysFont("comicsansms", 24)
        text = font.render(string, True, (0, 0, 255), Color_White)  # 綠色底，藍色字 (R,G,B)
        screen.blit(text, (250, 100))
        pygame.display.update()
        time.sleep(3)

        pygame.quit()  # 關閉繪圖視窗

# =================================
# num = select_num_of_player()
#
# print(num)
