import pygame
import sys
from screen import *
from snake import *
from food import *

class Game:
    running = True

    def __init__(self):
        # Создаем игру и окно
        pygame.init()
        pygame.mixer.init()

        self.clock = pygame.time.Clock()
        self.screen = Screen()
        self.snake = Snake()
        self.food = Food()

    def run(self):
        # Цикл игры
        while self.running:
            # Держим цикл на правильной скорости
            self.clock.tick(FPS)
            # Ввод процесса (события)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    self.handle_movement(event)
            blocks = self.snake.blocks[:]
            blocks.append(self.food.block)
            self.screen.draw(blocks)
            if not self.running:
                pygame.quit()

    def handle_movement(self, event):
        if event.key == pygame.K_LEFT:
            self.snake.move(-1, 0)
        elif event.key == pygame.K_RIGHT:
            self.snake.move(1, 0)
        elif event.key == pygame.K_UP:
            self.snake.move(0, -1)
        elif event.key == pygame.K_DOWN:
            self.snake.move(0, 1)
