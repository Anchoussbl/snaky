from block import *
from screen import YELLOW

class Food:
    color = YELLOW
    block = None

    def __init__(self):
        self.block = Block(8, 2, self.color)