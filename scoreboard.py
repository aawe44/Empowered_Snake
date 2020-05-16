import pygame


class Scoreboard:
    def __init__(self, screen, snakes):

        self.screen = screen
        self.snakes = snakes
        self.num_of_player = len(self.snakes)

    def update(self):

        for i in range(self.num_of_player):
            string = " ".join(["player", str(i + 1), ":", str(self.snakes[i].score)])

            if self.snakes[i].inevitable:
                count_down = (100 - self.snakes[i].inevitable_cnt) // 10
                string += " now is inevitable, count down: " + str(count_down)

            font = pygame.font.SysFont("comicsansms", 16)
            text = font.render(string, True, (0, 0, 255), (0, 255, 0))  # 綠色底，藍色字 (R,G,B)
            self.screen.blit(text, (0, 0 + i * 20))
