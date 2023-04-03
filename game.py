from food import *
from screen import *
from snake import *
from menu import *
from pause import *
from record import *
from game_state import *
import random


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
        self.menu = Menu()
        self.pause = Pause()
        self.record = Record()
        self.place_food()
        self.state = GameState.Menu
        self.b_turns = []
        self.score = 0
        self.speed = 1000
        self.rec = 0


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
                    if self.state == GameState.Running:
                        self.handle_direction_change(event)
                        if event.key == pygame.K_ESCAPE:
                            self.state = GameState.Pause
                    elif self.state == GameState.Menu:
                        self.menu.handle_press(self, event.key)
                    elif self.state == GameState.Pause:
                        self.pause.handle_press(self, event.key)
                    elif self.state == GameState.Record:
                        self.record.handle_press(self, event.key)


            if time_elapsed > self.speed:
                # Обновляем логику игры
                if self.state == GameState.Running:
                    self.tick()
                    time_elapsed = 0

            if self.state == GameState.Running:
                self.screen.reset()
                # Рисуем решетку
                self.screen.draw_grid()
                self.screen.draw_block(self.food.block)
                for block in self.snake.blocks:
                    self.screen.draw_block(block)
                self.screen.draw_text(str(self.score))
                self.screen.draw_text(str("record: {}".format(self.rec)), x=80, y=10)
                self.screen.update()
            elif self.state == GameState.Menu:
                # отрисовываем меню
                self.handle_menu()
            elif self.state == GameState.Pause:
                # отрисовываем паузу
                self.handle_pause()
            elif self.state == GameState.Record:
                self.record.show(self)



        if not self.running:
            self.game_over()

    def tick(self):
        self.handle_movement()
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
            self.score += 1
            if self.score > self.rec:
                self.rec += 1

            if self.speed >= 600:
                self.speed -= 100
            elif self.speed >= 400:
                self.speed -= 50
            else:
                self.speed -= 10

    def handle_menu(self):
        self.menu.show(self)

    def handle_pause(self):
        self.pause.show(self)

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
        self.running = False

    def place_food(self):
        self.food.block.x = random.randint(0, 9)
        self.food.block.y = random.randint(0, 9)
        while self.food.block in self.snake.blocks:
            self.food.block.x = random.randint(0, 9)
            self.food.block.y = random.randint(0, 9)

    def reset(self):
        self.screen = Screen()
        self.snake = Snake()
        self.food = Food()
        self.place_food()
        self.state = GameState.Menu
        self.b_turns = []
        self.score = 0
        self.speed = 1000
