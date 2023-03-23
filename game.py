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
        self.b_turns = []

        self.key_to_dir = {pygame.K_UP: Direction.Up,
                           pygame.K_DOWN: Direction.Down,
                           pygame.K_LEFT: Direction.Left,
                           pygame.K_RIGHT: Direction.Right,
                           pygame.K_w: Direction.Up,
                           pygame.K_s: Direction.Down,
                           pygame.K_a: Direction.Left,
                           pygame.K_d: Direction.Right}

    def run(self):
        # Цикл игры
        time_elapsed = 0
        while self.running:
            time_elapsed += self.clock.tick()
            # Ввод процесса (события)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    direction = self.key_to_dir.get(event.key, None)
                    if direction is not None:
                        self.b_turns.append(Block(self.snake.blocks[0].x, self.snake.blocks[0].y, direction=direction))

            if time_elapsed > 1000:
                # Обновляем логику игры
                self.handle_movement()
                time_elapsed = 0

            blocks = self.snake.blocks[:]
            blocks.append(self.food.block)
            self.screen.draw(blocks)
            if not self.running:
                pygame.quit()

    def handle_movement(self):
        for b in self.snake.blocks:
            if len(self.b_turns) > 0:
                for t in self.b_turns:
                    if b == t:
                        b.direction = t.direction
                        if b == self.snake.blocks[-1]:
                            self.b_turns.pop(0)
            if b.direction == Direction.Up:
                b.y -= 1
            elif b.direction == Direction.Down:
                b.y += 1
            elif b.direction == Direction.Left:
                b.x -= 1
            elif b.direction == Direction.Right:
                b.x += 1
