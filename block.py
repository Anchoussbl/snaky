from enum import Enum

class Direction(Enum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3

class Block:
    def __init__(self, x=0, y=0, color=None, direction=None):
        self.x = x
        self.y = y
        self.color = color
        self.direction = direction

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

