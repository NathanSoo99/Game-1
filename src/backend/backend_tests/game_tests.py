import pytest

from ..GameData import game_data
from ..Game import Game

setup = game_data["setup"]

def test_game_initialize():
    game = Game()

    assert len(game.board) == len(game_data["setup"])