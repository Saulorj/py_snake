import global_util as gb
from random import randint
import pygame
from pygame.locals import *


class Apple:
    def __init__(self, screen, game_area):
        self.size = gb.square_size
        self.apple_color = gb.color_red
        self.screen = screen
        self.game_area = game_area
        self.rect = None
        self.update()

    def draw(self):
        pos = (self.x_apple, self.y_apple, self.size, self.size)
        self.rect = pygame.draw.rect(self.screen, self.apple_color, pos)

    def get_rect(self):
        return self.rect

    def update(self):
        x = randint(0, gb.matrix[0]-1)
        y = randint(0, gb.matrix[1]-1)
        x,y = gb.convert_matrix_game_area(x,y, self.game_area)
        self.x_apple = x
        self.y_apple = y