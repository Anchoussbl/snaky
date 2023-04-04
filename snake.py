from block import *
from screen import GREEN
class Snake:
    color = GREEN
    blocks = []

    def __init__(self):
        self.blocks = [Block(4, 4, self.color, Direction.Up),
                       Block(4, 5, self.color, Direction.Up)]

    def move(self, offset_x, offset_y):
        for b in self.blocks:
            b.x += offset_x
            b.y += offset_y

    def add_block(self):
        last_block = self.blocks[-1]
        new_block = Block(last_block.x, last_block.y, self.color, last_block.direction)
        self.blocks.append(new_block)
        if new_block.direction == Direction.Up:
            new_block.y += 1
        if new_block.direction == Direction.Down:
            new_block.y -= 1
        if new_block.direction == Direction.Left:
            new_block.x += 1
        if new_block.direction == Direction.Right:
            new_block.x -= 1
