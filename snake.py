from block import *
from screen import GREEN


class Snake:
    color = GREEN
    blocks = []

    def __init__(self):
        self.blocks = [Block(4, 4, self.color, Direction.Up),
                       Block(4, 5, self.color, Direction.Up),
                       Block(4, 6, self.color, Direction.Up),
                       Block(4, 7, self.color, Direction.Up)]

    def move(self, offset_x, offset_y):
        for b in self.blocks:
            b.x += offset_x
            b.y += offset_y
