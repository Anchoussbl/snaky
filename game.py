import random

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
        self.place_food()
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
        score = 0
        time_elapsed = 0
        while self.running:
            time_elapsed += self.clock.tick()
            # Ввод процесса (события)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    self.handle_direction_change(event)

            if time_elapsed > 1000:
                # Обновляем логику игры
                self.handle_movement()
                time_elapsed = 0

            blocks = self.snake.blocks[:]
            blocks.append(self.food.block)
            self.screen.draw(blocks)
            self.screen.draw_text(str(score))
            self.screen.update()

            for block in self.snake.blocks:
                if block.x < 0 or block.y < 0 or \
                        block.x >= 10 or block.y >= 10:
                    self.running = False

            for block in self.snake.blocks:
                count = 0
                for b in self.snake.blocks:
                    if block == b:
                        count += 1
                if count > 1:
                    self.running = False

            if self.snake.blocks[0] == self.food.block:
                self.place_food()
                self.snake.add_block()
                score += 1

        if not self.running:
            self.game_over()

    def handle_direction_change(self, event):
        direction = self.key_to_dir.get(event.key, None)
        d = self.snake.blocks[0].direction
        if ((direction == Direction.Up or direction == Direction.Down) and
            (d == Direction.Left or d == Direction.Right)) or \
                ((direction == Direction.Left or direction == Direction.Right) and
                 (d == Direction.Up or d == Direction.Down)):
            self.b_turns.append(Block(self.snake.blocks[0].x, self.snake.blocks[0].y, direction=direction))

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

    def game_over(self):
        pygame.quit()

    def place_food(self):
        self.food.block.x = random.randint(0, 9)
        self.food.block.y = random.randint(0, 9)
        while self.food.block in self.snake.blocks:
            self.food.block.x = random.randint(0, 9)
            self.food.block.y = random.randint(0, 9)
