## game.py

import curses
import random
from snake import Snake
from apple import Apple


class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.score = 0
        self.snake = Snake()
        self.apple = Apple()

    def start_game(self):
        while True:
            action = self.stdscr.getch()
            self.snake.move(action)

            if self.snake.body[0] == self.apple.position:
                self.apple.respawn()
                self.snake.grow()
                self.score += 1

            self.draw()

            if self.is_game_over():
                break

        self.end_game()

    def draw(self):
        self.stdscr.clear()

        for segment in self.snake.body:
            self.stdscr.addch(segment[0], segment[1], curses.ACS_CKBOARD)

        self.stdscr.addch(self.apple.position[0], self.apple.position[1], curses.ACS_DIAMOND)
        self.stdscr.addstr(0, 0, f"Score: {self.score}")
        self.stdscr.refresh()

    def is_game_over(self):
        if (self.snake.body[0][0] in [0, curses.LINES - 1] or
            self.snake.body[0][1] in [0, curses.COLS - 1]):
            return True

        if self.snake.body[0] in self.snake.body[1:]:
            return True

        return False

    def end_game(self):
        self.stdscr.clear()
        self.stdscr.addstr(curses.LINES // 2, (curses.COLS - len(f"Game Over! Final Score: {self.score}")) // 2,
                           f"Game Over! Final Score: {self.score}")
        self.stdscr.refresh()
        self.stdscr.getch()
