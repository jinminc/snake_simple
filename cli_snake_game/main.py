## main.py

import curses
from game import Game

def main(stdscr):
    # Set up the screen
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Create a game instance
    game = Game(stdscr)

    # Start the game
    game.start_game()

if __name__ == "__main__":
    curses.wrapper(main)
