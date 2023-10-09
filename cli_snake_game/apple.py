import random
import curses

class Apple:
    def __init__(self):
        self.position = self.respawn()

    def respawn(self):
        self.position = (random.randint(1, curses.LINES - 2), random.randint(1, curses.COLS - 2))
        return self.position
