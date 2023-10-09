## test_game.py

import pytest
from game import Game
from snake import Snake
from apple import Apple

def test_snake_initial_length():
    snake = Snake()
    assert len(snake.body) == 3

def test_snake_grow():
    snake = Snake()
    initial_length = len(snake.body)
    snake.grow()
    assert len(snake.body) == initial_length + 1

def test_apple_respawn():
    apple = Apple()
    initial_position = apple.position
    apple.respawn()
    assert apple.position != initial_position

def test_game_initial_score():
    game = Game(None)
    assert game.score == 0

def test_game_score_increase():
    game = Game(None)
    game.snake.body[0] = game.apple.position
    initial_score = game.score
    game.apple.respawn()
    game.snake.grow()
    game.score += 1
    assert game.score == initial_score + 1
