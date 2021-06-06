import global_util as gb
import pygame
from pygame.locals import *
from random import randint



class Snake:
    def __init__(self, screen, game_area):
        self.screen = screen
        self.size = gb.square_size
        self.game_area = game_area
        self.speed = 5
        self.x_snake = 0
        self.y_snake = 0
        self.snake_lenght = 0
        self.pos_body = []
        self.pos_head = []
        self.randon_direction()
        self.rect = None

    def randon_direction(self):
        directions = ['l', 'r', 'u', 'd']
        direction = directions[randint(0,3)]

        x = randint(0, gb.matrix[0]-1)
        y = randint(0, gb.matrix[1]-1)
        x,y = gb.convert_matrix_game_area(x,y, self.game_area)
        self.x_snake = x
        self.y_snake = y

        if (direction == 'l'):
            self.x_direction = -self.speed
            self.y_direction = 0
        elif (direction == 'r'):
            self.x_direction = self.speed
            self.y_direction = 0
        elif (direction == 'u'):
            self.x_direction = 0
            self.y_direction = -self.speed
        elif (direction == 'd'):
            self.x_direction = 0
            self.y_direction = self.speed

        self.global_direction = direction

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

    def get_rect(self):
        return self.rect

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
        self.rect = pygame.draw.rect(self.screen, color, pos_head)

        x_eye1 = 0
        x_eye2 = 0
        y_eye1 = 0
        y_eye2 = 0

        if (self.global_direction == 'l'):
            x_eye1 = pos_head[0] + (self.size // 4)
            x_eye2 = pos_head[0] + (self.size // 4)
            y_eye1 = pos_head[1] + (self.size // 6 )
            y_eye2 = pos_head[1] + (self.size * 0.8)
        elif (self.global_direction == 'r'):
            x_eye1 = pos_head[0] + self.size - (self.size // 4)
            x_eye2 = pos_head[0] + self.size - (self.size // 4)
            y_eye1 = pos_head[1] + (self.size // 6)
            y_eye2 = pos_head[1] + (self.size * 0.8)
        elif (self.global_direction == 'u'):
            x_eye1 = pos_head[0] + (self.size // 4)
            x_eye2 = pos_head[0] + self.size - (self.size // 4)
            y_eye1 = pos_head[1] + (self.size // 5)
            y_eye2 = pos_head[1] + (self.size // 5)
        elif (self.global_direction == 'd'):
            x_eye1 = pos_head[0] + self.size - (self.size // 4)
            x_eye2 = pos_head[0] + (self.size // 4)
            y_eye1 = pos_head[1] + (self.size * 0.8)
            y_eye2 = pos_head[1] + (self.size * 0.8)

        eye_size = int(self.size * 0.15)
        pygame.draw.circle(self.screen, gb.color_red, (x_eye1, y_eye1),eye_size)
        pygame.draw.circle(self.screen, gb.color_red, (x_eye2, y_eye2),eye_size)
