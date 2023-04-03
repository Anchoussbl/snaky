import pygame

from screen import WIDTH, GREY, RED, HEIGHT
from game_state import *

class Record:
    def handle_press(self, game, key):
        if key == pygame.K_RETURN:
            game.state = GameState.Menu

    def show(self, game):
        game.screen.reset()
        game.screen.draw_text("Current record: {}".format(game.rec), x=WIDTH/2, y=HEIGHT/2 - 60, color=RED)
        game.screen.draw_text("Back", x=WIDTH/2, y=HEIGHT/2)
        game.screen.update()
