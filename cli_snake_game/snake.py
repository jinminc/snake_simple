## snake.py

import curses

class Snake:
    def __init__(self):
        self.body = [[10, 10], [10, 9], [10, 8]]

    def move(self, action):
        head = list(self.body[0])

        if action == curses.KEY_UP:
            head[0] -= 1
        elif action == curses.KEY_DOWN:
            head[0] += 1
        elif action == curses.KEY_LEFT:
            head[1] -= 1
        elif action == curses.KEY_RIGHT:
            head[1] += 1
        else:
            # If no key is pressed continue in the current direction
            head = [self.body[0][0] + (self.body[0][0] - self.body[1][0]),
                    self.body[0][1] + (self.body[0][1] - self.body[1][1])]

        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])
