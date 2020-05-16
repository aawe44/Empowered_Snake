import random
import pygame

Color_White = (255, 255, 255)
Color_Black = (0, 0, 0)
Color_Red = (255, 0, 0)
Color_Green = (0, 255, 0)
Color_Blue = (0, 0, 255)


class Food:
    def __init__(self, step_size, background):
        self.step_size = step_size
        self.background = background
        self.pos = None
        self.inevitable = False
        self.create()

    def create(self):
        fx, fy = random.randint(5, 63) * self.step_size, random.randint(5, 31) * self.step_size
        self.pos = [fx, fy]
        self.inevitable = random.randint(0, 9) >= 5

    def show(self):
        fx, fy = self.pos
        color = Color_Black if self.inevitable else Color_Red
        pygame.draw.rect(self.background, color, [fx, fy, 10, 10])
