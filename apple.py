import global_util as gb
from random import randint
import pygame
from pygame.locals import *


class Apple:
    def __init__(self, screen):
        self.size = 20
        self.x_apple = randint(40, 600)
        self.y_apple = randint(50, 430)
        self.apple_color = gb.color_red
        self.screen = screen

    def draw(self):
        pos = (self.x_apple, self.y_apple, self.size, self.size)
        return pygame.draw.rect(self.screen, self.apple_color, pos)

    def update(self):
        self.x_apple = randint(40, 600)
        self.y_apple = randint(50, 430)