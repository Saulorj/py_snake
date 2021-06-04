import pygame
from pygame.locals import *
from sys import exit
from random import randint
import global_util as gb
from snake import Snake
from apple import Apple

class Game:
    def __init__(self):
        pygame.init()
        self.width = gb.width
        self.height = gb.height
        self.back_ground_color = gb.color_white
        self.font_color =gb.color_white
        self.points = 0
        self.font = pygame.font.SysFont('arial', 20, bold=True, italic=False)
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Python Snake Game')
        self.snk = Snake(self.screen)
        self.apple = Apple(self.screen)

    def update_game_stats(self):
        message = f'Points: {self.points}'
        text = self.font.render(message, True, gb.color_white)
        self.screen.blit(text, (20,10))

    def draw(self):
        # Background
        self.screen.fill(self.back_ground_color)

        # left control panel
        pos_pnl_left = (0,0, gb.width//3, gb.height)
        pygame.draw.rect(self.screen, gb.color_black, pos_pnl_left)

        # snake border
        pygame.draw.rect(self.screen, gb.color_grey, (gb.width//3, 0, gb.width, gb.height), gb.border)

        # game border
        pygame.draw.rect(self.screen, gb.color_grey, (0, 0, gb.width, gb.height), gb.border)

        # game area
        start_w = ((gb.width+gb.border)//3)
        cells = (gb.width - start_w) // self.snk.size
        x = start_w
        for cell in range(cells):
            x = x + self.snk.size
            pos_start = (x, 0)
            pos_end = (x, gb.height)
            pygame.draw.line(self.screen, gb.color_grey, pos_start, pos_end)


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

            # upgrade position automatically
            self.snk.move_it()
            snake_obj = self.snk.draw()
            apple_obj = self.apple.draw()

            points = self.test_collide(snake_obj, apple_obj)
            self.update_game_stats()

            pygame.display.flip()
            #pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()