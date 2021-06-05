import global_util as gb
import pygame
from pygame.locals import *


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.size = gb.square_size
        self.speed = 5
        self.x_snake = gb.width/2
        self.y_snake = gb.height/2
        self.snake_lenght = 0
        self.pos_body = []
        self.pos_head = []
        self.x_direction = -self.speed
        self.y_direction = 0
        self.global_direction = 'l' #l, r, u, d


    def move_lef(self):
        if self.x_direction > 0: #block if going to right
            pass
        else:
            self.global_direction = 'l'
            self.x_direction = -self.speed
            self.y_direction = 0

    def move_right(self):
        if self.x_direction < 0: #block if going to left
            pass
        else:
            self.global_direction = 'r'
            self.x_direction = self.speed
            self.y_direction = 0

    def move_up(self):
        if self.y_direction > 0: #blobk if going to down
            pass
        else:
            self.global_direction = 'u'
            self.x_direction = 0
            self.y_direction = -self.speed

    def move_down(self):
        if self.y_direction < 0: #blobk if going to up
            pass
        else:
            self.global_direction = 'd'
            self.x_direction = 0
            self.y_direction = self.speed

    def move_it(self):
        self.y_snake = self.y_snake + self.y_direction
        self.x_snake = self.x_snake + self.x_direction

    def grow_up(self):
        self.snake_lenght = self.snake_lenght + 1

    def draw(self):
        self.pos_body.append((self.x_snake, self.y_snake))

        if (len(self.pos_body) > self.snake_lenght):
            del self.pos_body[0]

        color = gb.color_green
        # desenha o corpo
        for pos in self.pos_body:
            pos_body = (pos[0], pos[1], self.size, self.size)
            pygame.draw.rect(self.screen, color, pos_body)

        # desenha a cabeça
        pos_head = (self.x_snake, self.y_snake, self.size, self.size)
        rect = pygame.draw.rect(self.screen, color, pos_head)

        x_eye = self.size // 4
        y_eye1 = self.size // 6
        y_eye2 = self.size * 0.8
        eye_size = int(self.size * 0.15)
        pygame.draw.circle(self.screen, gb.color_red, (pos_head[0]+x_eye, pos_head[1]+y_eye1),eye_size)
        pygame.draw.circle(self.screen, gb.color_red, (pos_head[0]+x_eye, pos_head[1]+y_eye2),eye_size)
        return rect
