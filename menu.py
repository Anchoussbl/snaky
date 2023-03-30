import pygame

from screen import WIDTH, GREY, WHITE
from game_state import *

class Menu:
    def __init__(self):
        self.entries = { "Start" : self.begin_game,
                         "Exit" : self.exit }
        self.keys_list = list(self.entries.keys())
        self.current_entry = 0

    def show(self, game):
        game.screen.reset()
        i = 100
        for k in self.entries.keys():
            c = GREY
            if k == self.keys_list[self.current_entry]:
                c = WHITE
            game.screen.draw_text(k, WIDTH / 2, i, c)
            i += 30
        game.screen.update()


    def handle_press(self, game, key):
        if key == pygame.K_RETURN:
            self.entries[self.keys_list[self.current_entry]](game)
        elif key == pygame.K_DOWN:
            self.current_entry += 1
            if self.current_entry >= len(self.keys_list):
                self.current_entry = 0
        elif key == pygame.K_UP:
            self.current_entry -= 1
            if self.current_entry < 0:
                self.current_entry = len(self.keys_list) - 1


    def begin_game(self, game):
        game.reset()
        game.state = GameState.Running

    def exit(self, game):
        game.game_over()
