import pygame

WIDTH = 360
HEIGHT = 360
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRID_LINE_WIDTH = 3


class Screen:
    def __init__(self):
        pygame.display.set_caption("Snaky")
        self.display = pygame.display.set_mode((WIDTH, HEIGHT + 40))

    def __draw_grid(self):
        x1 = 0
        y1 = HEIGHT / 10
        x2 = WIDTH
        y2 = HEIGHT / 10
        pygame.draw.line(self.display, WHITE, [x1, 40], [x2, 40], GRID_LINE_WIDTH) # Первая линия
        while y1 != HEIGHT and y2 != HEIGHT:
            pygame.draw.line(self.display, WHITE, [x1, y1 + 40], [x2, y2 + 40], GRID_LINE_WIDTH)
            y1 += HEIGHT / 10
            y2 += HEIGHT / 10

        x1 = WIDTH / 10
        y1 = 0
        x2 = WIDTH / 10
        y2 = HEIGHT
        while x1 != WIDTH and x2 != WIDTH:
            pygame.draw.line(self.display, WHITE, [x1, y1 + 40], [x2, y2 + 40], GRID_LINE_WIDTH)
            x1 += WIDTH / 10
            x2 += WIDTH / 10

    def draw_blocks(self, blocks):
        for block in blocks:
            if 10 >= block.x >= 0 and block.y <= 10 and block.y >= 0:
                pygame.draw.rect(self.display, block.color,
                                 (block.x * (WIDTH / 10) + 2.5, block.y * (HEIGHT / 10) + 2.5 + 40,
                                  WIDTH / 10 - GRID_LINE_WIDTH, HEIGHT / 10 - GRID_LINE_WIDTH))

    def draw(self, blocks):
        # Заливаем черным
        self.display.fill(BLACK)
        # Рисуем решетку
        self.__draw_grid()

        self.draw_blocks(blocks)

    def update(self):
        # После отрисовки всего, отображаем
        pygame.display.update()

    def draw_text(self, text):
        size, x, y = 18, WIDTH / 2, 10
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_display = font.render(text, True, WHITE)
        text_rect = text_display.get_rect()
        text_rect.midtop = (x, y)
        self.display.blit(text_display, text_rect)
