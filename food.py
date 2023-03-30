from block import *
from screen import YELLOW

class Food:
    color = YELLOW
    block = None

    def __init__(self, x=0, y=0):
        self.block = Block(x, y, self.color)