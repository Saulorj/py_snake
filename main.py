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
        self.back_ground_color = (255,255,255)
        self.font_color = (0,0,0)
        self.points = 0
        self.font = pygame.font.SysFont('arial', 30, bold=True, italic=True)
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Python Snake Game')
        self.snk = Snake(self.screen)
        self.apple = Apple(self.screen)

    def update_game_stats(self):
        message = f'Points: {self.points}'
        text = self.font.render(message, True, self.font_color)
        self.screen.blit(text, (450,40))

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
            relogio.tick(30)
            self.screen.fill(self.back_ground_color)

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

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()