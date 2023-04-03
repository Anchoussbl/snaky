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
GREY = (100, 100, 100)
GRID_LINE_WIDTH = 3


class Screen:
    def __init__(self):
        pygame.display.set_caption("Snaky")
        self.display = pygame.display.set_mode((WIDTH, HEIGHT + 40))

    def draw_grid(self):
        x = 0
        y = 0
        # горизонтальные линии
        while y < HEIGHT + 1:
            pygame.draw.line(self.display, WHITE, [x, y + 40], [WIDTH, y + 40], GRID_LINE_WIDTH)
            y += HEIGHT / 10

        x = 0
        y = 0
        # вертикальные линии
        while x < WIDTH + 1:
            pygame.draw.line(self.display, WHITE, [x, y + 40], [x, HEIGHT + 40], GRID_LINE_WIDTH)
            x += WIDTH / 10

    def draw_block(self, block):
        if 10 >= block.x >= 0 and block.y <= 10 and block.y >= 0:
            pygame.draw.rect(self.display, block.color,
                         (block.x * (WIDTH / 10) + 2.5, block.y * (HEIGHT / 10) + 2.5 + 40,
                          WIDTH / 10 - GRID_LINE_WIDTH, HEIGHT / 10 - GRID_LINE_WIDTH))


    def reset(self):
        # Заливаем черным
        self.display.fill(BLACK)

    def update(self):
        # После отрисовки всего, отображаем
        pygame.display.update()

    def draw_text(self, text, x=WIDTH / 2, y=10, color = WHITE):
        size = 23
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_display = font.render(text, True, color)
        text_rect = text_display.get_rect()
        text_rect.midtop = (x, y)
        self.display.blit(text_display, text_rect)
