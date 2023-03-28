from block import *
from screen import YELLOW
import random

class Food:
    color = YELLOW
    block = None

    def __init__(self, x=random.randint(0, 9), y=random.randint(0, 9)):
        self.block = Block(x, y, self.color)