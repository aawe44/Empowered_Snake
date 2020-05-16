import collections
import pygame

Screen_Width = 640
Screen_Height = 320

Color_White = (255, 255, 255)
Color_Black = (0, 0, 0)
Color_Red = (255, 0, 0)
Color_Green = (0, 255, 0)
Color_Blue = (0, 0, 255)

player_to_Color = {0: Color_Green, 1: Color_Blue}

Directions = {
    "U": [0, -1], "D": [0, 1],
    "R": [1, 0], "L": [-1, 0], }

rev_direct = {"U": "D", "D": "U", "R": "L", "L": "R"}

pyKey_to_direct_0 = {
    pygame.K_UP: "U", pygame.K_DOWN: "D",
    pygame.K_RIGHT: "R", pygame.K_LEFT: "L", }

pyKey_to_direct_1 = {
    pygame.K_w: "U", pygame.K_s: "D",
    pygame.K_d: "R", pygame.K_a: "L", }

player_to_KeyDirect = [pyKey_to_direct_0, pyKey_to_direct_1]


class Snake:
    def __init__(self, step_size, snake_length, player, background):
        self.step_size = step_size
        self.snake_length = snake_length
        self.background = background

        dx, dy = Screen_Width // 4 * (player + 1), Screen_Height // 4 * (player + 1)

        index = [i for i in range(snake_length)]

        self.body = collections.deque([[step_size * i + dx, dy] for i in index])

        self.visited = collections.defaultdict(int)

        for p in self.body:
            self.visited[tuple(p)] += 1

        self.head = None
        self.tail = None
        self.score = 0

        self.inevitable = False
        self.inevitable_cnt = 0

        self.player = player

        self.direct = "R"
        self.pre_direct = self.direct
        self.body_color = player_to_Color[player]
        self.pyKey_to_direct = player_to_KeyDirect[player]

        self.is_valid = True

    def move(self, ):
        running = True

        if self.inevitable:
            self.inevitable_cnt += 1

        if self.inevitable and self.inevitable_cnt > 100:
            self.inevitable = False
            self.inevitable_cnt = 0

        if self.direct == rev_direct[self.pre_direct]:
            self.direct = self.pre_direct

        self.pre_direct = self.direct

        self.tail = self.body.popleft()

        self.visited[tuple(self.tail)] -= 1

        if self.visited[tuple(self.tail)] == 0:
            del self.visited[tuple(self.tail)]

        step_size = self.step_size

        pygame.draw.rect(self.background , Color_White, [self.tail[0], self.tail[1], step_size, step_size])

        x, y = self.body[-1]
        dx, dy = Directions[self.direct]
        nx, ny = (x + step_size * dx) % Screen_Width, (y + step_size * dy) % Screen_Height

        self.head = [nx, ny]

        if tuple(self.head) in self.visited and not self.inevitable:
            running = False

        self.body.append([nx, ny])
        self.visited[(nx, ny)] += 1
        pygame.draw.rect(self.background , Color_Green, [nx, ny, step_size, step_size])

        if not running:
            self.is_valid = False

        return running

    def gorw(self):
        self.score += 1
        step_size = self.step_size

        self.body.appendleft(self.tail)
        self.visited[tuple(self.tail)] += 1

        pygame.draw.rect(self.background , self.body_color, [self.tail[0], self.tail[1], step_size, step_size])

    def show(self):

        cnt = 0

        for x, y in reversed([(x, y) for x, y in self.body]):
            color = Color_Black if self.inevitable and cnt % 2 == 1 else self.body_color
            pygame.draw.rect(self.background , color, [x, y, self.step_size, self.step_size])
            cnt += 1
