import pygame
from pygame.locals import *
from sys import exit
from random import randint
import global_util as gb
from snake import Snake
from apple import Apple

class Game:
    def __init__(self):
        self.state = gb.RUNNING
        self.width = 0
        self.height = 0
        self.back_ground_color = gb.color_white
        self.font_color =gb.color_white
        self.points = 0
        self.game_area = (0, 0, 0, 0)
        self.game_matrix = gb.matrix
        self.set_game_area()
        self.screen = self.set_pygame()
        self.create_objects()

    def create_objects(self):
        self.snk = Snake(self.screen, self.game_area)
        self.apple = Apple(self.screen, self.game_area)

    def set_pygame(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Python Snake Game')
        return screen

    def set_game_area(self):
        '''
          Set the game area based on game_matrix
        '''
        game_area = (self.game_matrix[0] * gb.square_size)
        game_area_start = game_area // 2
        self.width = game_area + game_area_start
        self.height = self.game_matrix[1] * gb.square_size
        self.game_area = (game_area_start, 0, self.width, self.height)
        self.control_area = (0, 0, game_area_start, self.height)

    def update_game_stats(self):
        point_font = pygame.font.SysFont('arial', 20, bold=True, italic=False)
        message = f'Points: {self.points}'
        text = point_font.render(message, True, gb.color_white)
        self.screen.blit(text, (20,10))

    def show_pause(self):
        point_font = pygame.font.SysFont('arial', 20, bold=True, italic=False)
        text = point_font.render("Game Pause", True, gb.color_white)
        self.screen.blit(text, (20,10))

    def show_end(self):
        point_font = pygame.font.SysFont('arial', 20, bold=True, italic=False)
        text = point_font.render("Game End", True, gb.color_white)
        self.screen.blit(text, (20,10))


    def draw(self):
        # Background
        self.screen.fill(self.back_ground_color)

        # left control panel
        pygame.draw.rect(self.screen, gb.color_black, self.control_area)

        # game area
        pygame.draw.rect(self.screen, gb.color_white, self.game_area)

        #draw X grid
        x = self.game_area[0]
        for cell in range(self.game_matrix[0]):
            x = x + self.snk.size
            pos_start = (x, 0)
            pos_end = (x, self.game_area[3])
            pygame.draw.line(self.screen, gb.color_grey, pos_start, pos_end)
        y = self.game_area[1]
        for cell in range(self.game_matrix[1]):
            y = y + self.snk.size
            pos_start = (self.game_area[0], y)
            pos_end = (self.game_area[2], y)
            pygame.draw.line(self.screen, gb.color_grey, pos_start, pos_end)
        #first line
        pos_start = (self.game_area[0], 0)
        pos_end = (self.game_area[2], 0)
        pygame.draw.line(self.screen, gb.color_grey, pos_start, pos_end)

    def test_collide(self):
        snake_rect = self.snk.get_rect()
        apple_rect = self.apple.get_rect()
        if snake_rect.colliderect(apple_rect):
            self.apple.update()
            self.snk.grow_up()
            self.points += 1
        self.test_border()

    def test_border(self):
        x_snake = self.snk.x_snake
        y_snake = self.snk.y_snake
        #bottom and right must subtract snake size becose de point of snake (x,y)
        #is on the upper left corner
        if (x_snake >= self.game_area[2]-self.snk.size or
            x_snake <= self.game_area[0] or
            y_snake >= self.game_area[3]-self.snk.size or
            y_snake <= self.game_area[1]):
            self.state = gb.END

    def start_game(self):
        self.points = 0
        self.create_objects()
        self.state = gb.RUNNING


    def run(self):
        '''
        Snake game main loops
        '''
        relogio = pygame.time.Clock()

        self.state = gb.RUNNING
        while True:
            relogio.tick(gb.frame_rate)
            self.draw()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_a: self.snk.move_lef()
                    if event.key == K_d: self.snk.move_right()
                    if event.key == K_w: self.snk.move_up()
                    if event.key == K_s: self.snk.move_down()
                    if event.key == pygame.K_p: self.state = gb.PAUSE
                    if event.key == pygame.K_r: self.state = gb.RUNNING
                    if event.key == pygame.K_t: self.start_game()

            self.snk.draw()
            self.apple.draw()

            if (self.state == gb.RUNNING):
                # upgrade position automatically
                self.snk.move_it()
                self.test_collide()
                self.update_game_stats()
            elif (self.state == gb.PAUSE):
                self.show_pause()
            elif (self.state == gb.END):
                self.show_end()

            pygame.display.flip()
            #pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()