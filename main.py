import pygame
from pygame.locals import *
from sys import exit
from random import randint
import global_util as gb
from snake import Snake
from apple import Apple

class Game:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.back_ground_color = gb.color_white
        self.font_color =gb.color_white
        self.points = 0
        self.game_area = (0, 0, 0, 0)
        self.game_matrix = gb.matrix
        self.set_game_area()
        self.screen = self.set_pygame()
        self.create_objects(self.screen)

    def create_objects(self, screen):
        self.snk = Snake(self.screen)
        self.apple = Apple(self.screen)


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
        pass

    def update_game_stats(self):
        point_font = pygame.font.SysFont('arial', 20, bold=True, italic=False)
        message = f'Points: {self.points}'
        text = point_font.render(message, True, gb.color_white)
        self.screen.blit(text, (20,10))

    def show_pause(self):
        point_font = pygame.font.SysFont('arial', 20, bold=True, italic=False)
        text = point_font.render("Game Pause", True, gb.color_white)
        self.screen.blit(text, (20,10))


    def draw(self):
        # Background
        self.screen.fill(self.back_ground_color)

        # left control panel
        pygame.draw.rect(self.screen, gb.color_black, self.control_area)

        # snake border
        #pygame.draw.rect(self.screen, gb.color_grey, (gb.width//3, 0, gb.width, gb.height), gb.border)

        # game border
        #pygame.draw.rect(self.screen, gb.color_grey, (0, 0, gb.width, gb.height), gb.border)

        # game area
        pygame.draw.rect(self.screen, gb.color_grey, self.game_area)
        '''
        start_w = ((gb.width+gb.border)//3)
        cells = (gb.width - start_w) // self.snk.size
        x = start_w
        for cell in range(cells):
            x = x + self.snk.size
            pos_start = (x, 0)
            pos_end = (x, gb.height)
            pygame.draw.line(self.screen, gb.color_grey, pos_start, pos_end)
        '''

    def test_collide(self, snake_object, apple_object):
        if snake_object.colliderect(apple_object):
            self.apple.update()
            self.snk.grow_up()
            self.points += 1

    def run(self):
        '''
        Snake game main loops
        '''
        relogio = pygame.time.Clock()
        RUNNING, PAUSE = 0, 1
        state = RUNNING
        while True:
            relogio.tick(gb.frame_rate)
            self.draw()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_a:
                        self.snk.move_lef()
                    if event.key == K_d:
                        self.snk.move_right()
                    if event.key == K_w:
                        self.snk.move_up()
                    if event.key == K_s:
                        self.snk.move_down()
                    if event.key == pygame.K_p: state = PAUSE
                    if event.key == pygame.K_r: state = RUNNING

            snake_obj = self.snk.draw()
            apple_obj = self.apple.draw()

            if (state == RUNNING):
                # upgrade position automatically
                self.snk.move_it()
                points = self.test_collide(snake_obj, apple_obj)
                self.update_game_stats()
            elif (state == PAUSE):
                self.show_pause()

            pygame.display.flip()
            #pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()